// frontend/src/ui/aurora-background/index.jsx
'use client'
import React from 'react'
import './aurora-background.css'

/**
 * AuroraBackground 组件
 * Props:
 *  - className: 附加到最外层容器的额外 class
 *  - children: 渲染在背景之上的内容
 */
export function AuroraBackground({ className = '', children, showRadialGradient = true, ...props }) {
  return (
    <main>
      <div
        className={`transition-bg relative flex h-[100vh] flex-col items-center justify-center bg-zinc-50 text-slate-950 dark:bg-zinc-900 ${className}`}
        {...props}
      >
        <div
          className="absolute inset-0 overflow-hidden animate-aurora"
          style={{
            '--aurora': 'repeating-linear-gradient(100deg,#3b82f6 10%,#a5b4fc 15%,#93c5fd 20%,#ddd6fe 25%,#60a5fa 30%)',
            '--dark-gradient': 'repeating-linear-gradient(100deg,#000 0%,#000 7%,transparent 10%,transparent 12%,#000 16%)',
            '--white-gradient': 'repeating-linear-gradient(100deg,#fff 0%,#fff 7%,transparent 10%,transparent 12%,#fff 16%)',
          }}
        >
          <div
            className={`after:animate-aurora pointer-events-none absolute -inset-[10px]
              [background-image:var(--white-gradient),var(--aurora)] [background-size:300%,_200%]
              [background-position:50%_50%,50%_50%] opacity-50 blur-[10px] invert filter will-change-transform
              after:absolute after:inset-0 after:[background-image:var(--white-gradient),var(--aurora)]
              after:[background-size:200%,_100%] after:[background-attachment:fixed]
              after:mix-blend-difference after:content-[''] dark:[background-image:var(--dark-gradient),var(--aurora)]
              dark:invert-0 after:dark:[background-image:var(--dark-gradient),var(--aurora)]`}
            style={ showRadialGradient ? { maskImage: 'radial-gradient(ellipse at 100% 0%, black 10%, transparent 70%)' } : {} }
          ></div>
        </div>
        {children}
      </div>
    </main>
  )
}
