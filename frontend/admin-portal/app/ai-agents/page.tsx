"use client";
import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { useQuery, useMutation } from "@tanstack/react-query";
import { aiApi } from "@/lib/api";
import { Brain, Package, Users, DollarSign, Briefcase, ShoppingCart, Factory, FolderKanban, ShieldCheck, BarChart3, MessageSquare, Play, Loader2 } from "lucide-react";
const categoryIcons: Record<string, any> = { Inventory: Package, CRM: Users, Finance: DollarSign, HR: Briefcase, Procurement: ShoppingCart, Manufacturing: Factory, Projects: FolderKanban, Compliance: ShieldCheck, Analytics: BarChart3, General: MessageSquare };
export default function AIAgentsPage() {
  const [selectedSkill, setSelectedSkill] = useState<string | null>(null);
  const [skillInput, setSkillInput] = useState("");
  const [chatMessage, setChatMessage] = useState("");
  const [chatSession, setChatSession] = useState<string | null>(null);
  const [chatHistory, setChatHistory] = useState<{role: string; content: string}[]>([]);
  const { data: skills } = useQuery({ queryKey: ["ai-skills"], queryFn: () => aiApi.getSkills().then(r => r.data) });
  const { data: runHistory } = useQuery({ queryKey: ["ai-runs"], queryFn: () => aiApi.getRunHistory().then(r => r.data) });
  const runMutation = useMutation({ mutationFn: ({ skill, data }: { skill: string; data: any }) => aiApi.runSkill(skill, data) });
  const chatMutation = useMutation({
    mutationFn: (message: string) => aiApi.chat(message, chatSession || undefined),
    onSuccess: (data) => { setChatSession(data.data.session_id); setChatHistory(prev => [...prev, { role: "assistant", content: data.data.response }]); },
  });
  const handleRunSkill = () => {
    if (!selectedSkill) return;
    try { const data = skillInput ? JSON.parse(skillInput) : {}; runMutation.mutate({ skill: selectedSkill, data }); }
    catch { runMutation.mutate({ skill: selectedSkill, data: { raw_input: skillInput } }); }
  };
  const handleChat = () => {
    if (!chatMessage.trim()) return;
    setChatHistory(prev => [...prev, { role: "user", content: chatMessage }]);
    chatMutation.mutate(chatMessage); setChatMessage("");
  };
  const skillsByCategory = skills?.skills?.reduce((acc: any, skill: any) => { acc[skill.category] = acc[skill.category] || []; acc[skill.category].push(skill); return acc; }, {});
  return (
    <div className="space-y-6">
      <div><h1 className="text-3xl font-bold tracking-tight">AI Agents</h1><p className="text-muted-foreground">15+ specialized AI skills for your ERP operations.</p></div>
      <div className="grid gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2 space-y-6">
          {skillsByCategory && Object.entries(skillsByCategory).map(([category, categorySkills]: [string, any]) => {
            const Icon = categoryIcons[category] || Brain;
            return (
              <Card key={category}>
                <CardHeader><CardTitle className="flex items-center gap-2"><Icon className="h-5 w-5 text-primary" />{category}</CardTitle><CardDescription>{categorySkills.length} AI skills available</CardDescription></CardHeader>
                <CardContent>
                  <div className="grid gap-2">
                    {categorySkills.map((skill: any) => (
                      <button key={skill.name} onClick={() => setSelectedSkill(skill.name)}
                        className={`flex items-center justify-between rounded-lg border p-3 text-left transition-colors hover:bg-accent ${selectedSkill === skill.name ? "border-primary bg-primary/5" : ""}`}>
                        <div><p className="font-medium">{skill.name.replace(/_/g, " ")}</p><p className="text-xs text-muted-foreground">{skill.description}</p></div>
                        <Badge variant="outline">{skill.name}</Badge>
                      </button>
                    ))}
                  </div>
                </CardContent>
              </Card>
            );
          })}
        </div>
        <div className="space-y-6">
          <Card>
            <CardHeader><CardTitle>Skill Runner</CardTitle><CardDescription>Execute AI skills with custom input</CardDescription></CardHeader>
            <CardContent className="space-y-4">
              <div><label className="text-sm font-medium">Selected Skill</label><p className="text-sm text-muted-foreground">{selectedSkill || "None selected"}</p></div>
              <div><label className="text-sm font-medium">Input (JSON)</label>
                <textarea value={skillInput} onChange={(e) => setSkillInput(e.target.value)} placeholder='{"product_id": "..."}' className="mt-1 min-h-[100px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm" /></div>
              <Button onClick={handleRunSkill} disabled={!selectedSkill || runMutation.isPending} className="w-full">
                {runMutation.isPending ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : <Play className="mr-2 h-4 w-4" />} Run Skill
              </Button>
              {runMutation.data && (
                <div className="rounded-md border bg-muted p-3">
                  <p className="text-xs font-medium">Result:</p>
                  <pre className="mt-1 max-h-40 overflow-auto text-xs">{JSON.stringify(runMutation.data.data, null, 2)}</pre>
                </div>
              )}
            </CardContent>
          </Card>
          <Card>
            <CardHeader><CardTitle>AI Chat</CardTitle><CardDescription>Ask questions about your ERP data</CardDescription></CardHeader>
            <CardContent className="space-y-4">
              <div className="max-h-60 space-y-2 overflow-auto rounded-md border bg-muted p-3">
                {chatHistory.length === 0 && <p className="text-xs text-muted-foreground">Start a conversation...</p>}
                {chatHistory.map((msg, i) => (
                  <div key={i} className={`rounded-lg px-3 py-2 text-sm ${msg.role === "user" ? "ml-4 bg-primary text-primary-foreground" : "mr-4 bg-background"}`}>{msg.content}</div>
                ))}
                {chatMutation.isPending && <div className="mr-4 rounded-lg bg-background px-3 py-2 text-sm"><Loader2 className="h-4 w-4 animate-spin" /></div>}
              </div>
              <div className="flex gap-2">
                <input type="text" value={chatMessage} onChange={(e) => setChatMessage(e.target.value)} onKeyDown={(e) => e.key === "Enter" && handleChat()}
                  placeholder="Ask about sales, inventory, employees..." className="flex-1 rounded-md border border-input bg-background px-3 py-2 text-sm" />
                <Button onClick={handleChat} disabled={chatMutation.isPending} size="sm"><MessageSquare className="h-4 w-4" /></Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
      {runHistory && runHistory.length > 0 && (
        <Card>
          <CardHeader><CardTitle>Recent Agent Runs</CardTitle></CardHeader>
          <CardContent>
            <div className="rounded-md border">
              <table className="w-full text-sm">
                <thead className="border-b bg-muted/50"><tr>
                  <th className="px-4 py-3 text-left">Agent</th><th className="px-4 py-3 text-left">Skill</th>
                  <th className="px-4 py-3 text-center">Status</th><th className="px-4 py-3 text-right">Tokens</th><th className="px-4 py-3 text-right">Duration</th>
                </tr></thead>
                <tbody>
                  {runHistory.slice(0, 10).map((run: any) => (
                    <tr key={run.id} className="border-b last:border-0">
                      <td className="px-4 py-3">{run.agent}</td><td className="px-4 py-3 font-mono text-xs">{run.skill}</td>
                      <td className="px-4 py-3 text-center"><Badge variant={run.status === "success" ? "success" : "danger"}>{run.status}</Badge></td>
                      <td className="px-4 py-3 text-right">{run.tokens}</td><td className="px-4 py-3 text-right">{run.duration_ms}ms</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
