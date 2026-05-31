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
import { generateText, Output } from 'ai';
import { MockLanguageModelV3 } from 'ai/test';
import { z } from 'zod';

const model = new MockLanguageModelV3({
  doGenerate: async () => ({
    content: [{ type: 'text', text: '{"recipe":{"name":"Toast","ingredients":[{"name":"Bread","amount":"2 slices"}],"steps":["Toast the bread","Serve warm"]}}' }],
    finishReason: { unified: 'stop', raw: undefined },
    usage: {
      inputTokens: { total: 4, noCache: 4, cacheRead: undefined, cacheWrite: undefined },
      outputTokens: { total: 12, text: 12, reasoning: undefined },
    },
    warnings: [],
  }),
});

const { output } = await generateText({
  model,
  output: Output.object({
    schema: z.object({
      recipe: z.object({
        name: z.string(),
        ingredients: z.array(
          z.object({
            name: z.string(),
            amount: z.string(),
          }),
        ),
        steps: z.array(z.string()),
      }),
    }),
  }),
  prompt: 'Generate a tiny recipe object.',
});

console.log(output);
