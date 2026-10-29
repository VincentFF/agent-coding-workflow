# Alternative Comparison

Use only when a consequential interface or ownership issue has multiple reasonable options; do not turn every design task into a competition.

Define shared goals, constraints, callers, and dependencies first, with a small example sufficient to illustrate the problem. The main agent compares necessary alternatives by default. Delegate read-only design tasks with distinct perspectives through the current runtime's subagent capabilities only when the user explicitly requests multiple agents or applicable instructions authorize delegation.

Each alternative describes its interface and important constraints, a usage example, hidden internals, dependency handling, and actual tradeoffs. Perspectives may include a minimal interface, common callers, or necessary flexibility; alternatives must differ beyond names or file layout.

Compare how much callers need to know, change locality, natural testability, and compatibility and migration costs. Give an evidence-based recommendation. Subagents do not modify project files or approve alternatives; the main agent refers consequential choices to the user. Do not start more than three agents by default or automatically write an ADR.
