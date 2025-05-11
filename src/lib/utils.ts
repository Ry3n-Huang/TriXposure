// src/lib/utils.ts
/**
 * 拼接 className，忽略 false/undefined/null
 */
export function cn(...classes: Array<string | false | undefined | null>) {
    return classes.filter(Boolean).join(" ");
  }
  