/*
(C) Copyright 2026 Boni Garcia (https://bonigarcia.github.io/)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
import { generateText, stepCountIs, tool } from 'ai';
import { MockLanguageModelV3 } from 'ai/test';
import { z } from 'zod';

let callCount = 0;

const model = new MockLanguageModelV3({
  doGenerate: async () => {
    callCount += 1;

    if (callCount === 1) {
      return {
        content: [
          {
            type: 'tool-call',
            toolCallId: 'tool-1',
            toolName: 'lookup',
            input: '{"term":"AI SDK"}',
          },
        ],
        finishReason: { unified: 'tool-calls', raw: undefined },
        usage: {
          inputTokens: { total: 6, noCache: 6, cacheRead: undefined, cacheWrite: undefined },
          outputTokens: { total: 4, text: 0, reasoning: undefined },
        },
        warnings: [],
      };
    }

    return {
      content: [{ type: 'text', text: 'The AI SDK is a set of building blocks for AI apps.' }],
      finishReason: { unified: 'stop', raw: undefined },
      usage: {
        inputTokens: { total: 8, noCache: 8, cacheRead: undefined, cacheWrite: undefined },
        outputTokens: { total: 12, text: 12, reasoning: undefined },
      },
      warnings: [],
    };
  },
});

const lookup = tool({
  description: 'Look up a short definition for a term',
  inputSchema: z.object({
    term: z.string(),
  }),
  execute: async ({ term }) => ({
    term,
    definition: 'A compact SDK for building AI features in JavaScript and TypeScript.',
  }),
});

const { text } = await generateText({
  model,
  tools: { lookup },
  stopWhen: stepCountIs(3),
  prompt: 'Use the lookup tool to define AI SDK, then answer in one sentence.',
});

console.log(text);
