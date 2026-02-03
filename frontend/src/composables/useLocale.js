import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { supportedLocales, setLocale as setI18nLocale } from '@/i18n'

export function useLocale() {
  const route = useRoute()
  const router = useRouter()
  const { locale, t, tm } = useI18n()

  // 当前语言
  const currentLocale = computed(() => locale.value)

  // 获取当前语言的路由前缀
  const localePrefix = computed(() => `/${locale.value}`)

  // 切换语言
  const switchLocale = (newLocale) => {
    if (!supportedLocales.includes(newLocale) || newLocale === locale.value) {
      return
    }

    // 更新 i18n 语言
    setI18nLocale(newLocale)

    // 获取当前路径（去除语言前缀）
    const currentPath = route.path
    let pathWithoutLocale = currentPath

    // 移除当前语言前缀
    for (const loc of supportedLocales) {
      if (currentPath.startsWith(`/${loc}/`) || currentPath === `/${loc}`) {
        pathWithoutLocale = currentPath.slice(loc.length + 1) || '/'
        break
      }
    }

    // 构建新路径
    const newPath = pathWithoutLocale === '/' 
      ? `/${newLocale}` 
      : `/${newLocale}${pathWithoutLocale}`

    // 导航到新路径
    router.push({ path: newPath, query: route.query })
  }

  // 生成带语言前缀的路径
  const localePath = (path) => {
    if (path.startsWith('/admin') || path.startsWith('/login')) {
      return path
    }
    const cleanPath = path.startsWith('/') ? path : `/${path}`
    return `/${locale.value}${cleanPath === '/' ? '' : cleanPath}`
  }

  return {
    currentLocale,
    localePrefix,
    switchLocale,
    localePath,
    t,
    tm,
    supportedLocales
  }
}





