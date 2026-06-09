import { defineConfig } from 'vitepress'

const base = process.env.CF_PAGES ? '/' : '/context-engineering/'

export default defineConfig({
  title: 'Context Engineering',
  description: 'Building Consistent, Accurate, Predictable AI Systems',
  outDir: '../dist',
  base,
  ignoreDeadLinks: false,

  head: [
    ['link', { rel: 'icon', href: `${base}favicon.ico` }]
  ],

  markdown: {
    config: (md) => {
      const defaultRender = md.renderer.rules.link_open || function(tokens, idx, options, env, self) {
        return self.renderToken(tokens, idx, options);
      };
      md.renderer.rules.link_open = function(tokens, idx, options, env, self) {
        const token = tokens[idx];
        const hrefIndex = token.attrIndex('href');
        if (hrefIndex >= 0) {
          const href = token.attrs[hrefIndex][1];
          const match = href.match(/^(?:\.\.\/)+ch(0[1-9]|1[0-2])\/(.+)$/);
          if (match) {
            token.attrs[hrefIndex][1] = `https://github.com/peanut996/context-engineering/blob/master/ch${match[1]}/${match[2]}`;
          }
        }
        return defaultRender(tokens, idx, options, env, self);
      };
    }
  },

  themeConfig: {
    nav: [
      { text: 'Guide', link: '/guide/' },
      { text: 'Tools', link: '/tools/' },
      {
        text: 'Language',
        items: [
          { text: 'English', link: '/' },
          { text: '中文', link: '/zh/' }
        ]
      }
    ],

    sidebar: {
      '/guide/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Introduction', link: '/guide/' },
            { text: 'Table of Contents', link: '/guide/table-of-contents' }
          ]
        },
        {
          text: 'Chapters',
          items: [
            { text: 'Ch1. Introduction', link: '/guide/ch01' },
            { text: 'Ch2. Instructions', link: '/guide/ch02' },
            { text: 'Ch3. External Knowledge', link: '/guide/ch03' },
            { text: 'Ch4. Tools', link: '/guide/ch04' },
            { text: 'Ch5. Memory & State', link: '/guide/ch05' },
            { text: 'Ch6. User Prompts', link: '/guide/ch06' },
            { text: 'Ch7. Context Management', link: '/guide/ch07' },
            { text: 'Ch8. Evaluation', link: '/guide/ch08' },
            { text: 'Ch9. Governance', link: '/guide/ch09' },
            { text: 'Ch10. AI Frameworks', link: '/guide/ch10' },
            { text: 'Ch11. Software Development', link: '/guide/ch11' },
            { text: 'Ch12. State of the Art', link: '/guide/ch12' }
          ]
        },
        {
          text: 'Appendix',
          items: [
            { text: 'A. AI Ecosystem', link: '/guide/appendix-a' },
            { text: 'B. References', link: '/guide/appendix-b' }
          ]
        }
      ],
      '/zh/guide/': [
        {
          text: '入门',
          items: [
            { text: '简介', link: '/zh/guide/' },
            { text: '目录', link: '/zh/guide/table-of-contents' }
          ]
        },
        {
          text: '章节',
          items: [
            { text: 'Ch1. 引言', link: '/zh/guide/ch01' },
            { text: 'Ch2. 指令', link: '/zh/guide/ch02' },
            { text: 'Ch3. 外部知识', link: '/zh/guide/ch03' },
            { text: 'Ch4. 工具', link: '/zh/guide/ch04' },
            { text: 'Ch5. 记忆与状态', link: '/zh/guide/ch05' },
            { text: 'Ch6. 用户提示词', link: '/zh/guide/ch06' },
            { text: 'Ch7. 上下文管理', link: '/zh/guide/ch07' },
            { text: 'Ch8. 评估与可观测性', link: '/zh/guide/ch08' },
            { text: 'Ch9. 治理与运维', link: '/zh/guide/ch09' },
            { text: 'Ch10. AI 框架', link: '/zh/guide/ch10' },
            { text: 'Ch11. 软件开发', link: '/zh/guide/ch11' },
            { text: 'Ch12. 前沿进展', link: '/zh/guide/ch12' }
          ]
        },
        {
          text: '附录',
          items: [
            { text: 'A. AI 生态', link: '/zh/guide/appendix-a' },
            { text: 'B. 参考资料', link: '/zh/guide/appendix-b' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/peanut9961/context-engineering' }
    ],

    footer: {
      message: 'Released under the Apache-2.0 License.',
      copyright: 'Copyright © 2026 Boni García'
    }
  },

  locales: {
    root: {
      label: 'English',
      lang: 'en'
    },
    zh: {
      label: '中文',
      lang: 'zh-CN',
      themeConfig: {
        nav: [
          { text: '指南', link: '/zh/guide/' },
          { text: '工具', link: '/zh/tools/' },
          {
            text: '语言',
            items: [
              { text: 'English', link: '/' },
              { text: '中文', link: '/zh/' }
            ]
          }
        ],
        sidebar: {
          '/zh/guide/': [
            {
              text: '入门',
              items: [
                { text: '简介', link: '/zh/guide/' },
                { text: '目录', link: '/zh/guide/table-of-contents' }
              ]
            },
            {
              text: '章节',
              items: [
                { text: 'Ch1. 引言', link: '/zh/guide/ch01' },
                { text: 'Ch2. 指令', link: '/zh/guide/ch02' },
                { text: 'Ch3. 外部知识', link: '/zh/guide/ch03' },
                { text: 'Ch4. 工具', link: '/zh/guide/ch04' },
                { text: 'Ch5. 记忆与状态', link: '/zh/guide/ch05' },
                { text: 'Ch6. 用户提示词', link: '/zh/guide/ch06' },
                { text: 'Ch7. 上下文管理', link: '/zh/guide/ch07' },
                { text: 'Ch8. 评估与可观测性', link: '/zh/guide/ch08' },
                { text: 'Ch9. 治理与运维', link: '/zh/guide/ch09' },
                { text: 'Ch10. AI 框架', link: '/zh/guide/ch10' },
                { text: 'Ch11. 软件开发', link: '/zh/guide/ch11' },
                { text: 'Ch12. 前沿进展', link: '/zh/guide/ch12' }
              ]
            },
            {
              text: '附录',
              items: [
                { text: 'A. AI 生态', link: '/zh/guide/appendix-a' },
                { text: 'B. 参考资料', link: '/zh/guide/appendix-b' }
              ]
            }
          ]
        },
        footer: {
          message: '基于 Apache-2.0 许可发布。',
          copyright: 'Copyright © 2026 Boni García'
        }
      }
    }
  }
})
