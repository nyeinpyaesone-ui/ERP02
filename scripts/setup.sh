set -e

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║          AI ERP System - One-Command Deployer              ║"
echo "║              Version 2.0.0-final | AI-Native ERP           ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

if [ ! -f .env ]; then
    echo -e "${BLUE}Generating secure .env credentials...${NC}"
    cat > .env <<EOF
# Database
DB_USER=erp_admin
DB_PASSWORD=$(openssl rand -base64 32 | tr -d '=+/' | cut -c1-24)
DB_NAME=ai_erp

# Redis
REDIS_URL=redis://redis:6379/0

# RabbitMQ
RABBITMQ_USER=erp_user
RABBITMQ_PASS=$(openssl rand -base64 32 | tr -d '=+/' | cut -c1-24)
RABBITMQ_URL=amqp://erp_user:${RABBITMQ_PASS}@rabbitmq:5672/

# Security
SECRET_KEY=$(openssl rand -hex 32)

# AI
OLLAMA_BASE_URL=http://ollama:11434

# Grafana
GRAFANA_PASS=$(openssl rand -base64 16 | tr -d '=+/')

# Feature Flags
ENABLE_AI_AGENTS=true
ENABLE_REALTIME_SYNC=true
ENABLE_AUDIT_LOG=true
ENABLE_RATE_LIMITING=true
EOF
    echo -e "${GREEN}✓ .env created with secure credentials${NC}"
fi

export $(grep -v '^#' .env | xargs)

echo -e "${BLUE}Starting infrastructure services...${NC}"
docker-compose -f infrastructure/docker-compose.yml up -d postgres redis rabbitmq

echo -e "${YELLOW}Waiting for services to be healthy...${NC}"
sleep 15

echo -e "${BLUE}Pulling AI models (this may take a while)...${NC}"
docker-compose -f infrastructure/docker-compose.yml up -d ollama
sleep 10

docker exec erp-ollama ollama pull llama3.1 || true
docker exec erp-ollama ollama pull mistral || true
docker exec erp-ollama ollama pull codellama || true
docker exec erp-ollama ollama pull nomic-embed-text || true

echo -e "${GREEN}✓ AI models downloaded${NC}"

echo -e "${BLUE}Running database migrations...${NC}"
docker-compose -f infrastructure/docker-compose.yml run --rm backend     python -c "import asyncio; from app.db.session import init_db; asyncio.run(init_db())"

echo -e "${GREEN}✓ Database initialized${NC}"

echo -e "${BLUE}Starting all services...${NC}"
docker-compose -f infrastructure/docker-compose.yml up -d

echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║              AI ERP System Deployed Successfully!            ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BLUE}Access Points:${NC}"
echo -e "  • Admin Portal:     ${YELLOW}http://localhost:3000${NC}"
echo -e "  • Client Dashboard:   ${YELLOW}http://localhost:3001${NC}"
echo -e "  • API Documentation:  ${YELLOW}http://localhost:8000/docs${NC}"
echo -e "  • RabbitMQ Console:   ${YELLOW}http://localhost:15672${NC}"
echo -e "  • Grafana:            ${YELLOW}http://localhost:3002${NC}"
echo -e "  • Prometheus:         ${YELLOW}http://localhost:9090${NC}"
echo ""
echo -e "${GREEN}All systems operational. AI agents ready for action.${NC}"