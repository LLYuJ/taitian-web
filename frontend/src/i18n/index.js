import { createI18n } from 'vue-i18n'
import zh from './locales/zh'
import en from './locales/en'

// 获取默认语言
function getDefaultLocale() {
  // 优先从 URL 中获取语言
  const pathLocale = window.location.pathname.split('/')[1]
  if (pathLocale === 'en' || pathLocale === 'zh') {
    return pathLocale
  }
  
  // 其次从 localStorage 中获取
  const savedLocale = localStorage.getItem('locale')
  if (savedLocale && (savedLocale === 'zh' || savedLocale === 'en')) {
    return savedLocale
  }
  
  // 最后根据浏览器语言判断
  const browserLang = navigator.language || navigator.userLanguage
  return browserLang.startsWith('zh') ? 'zh' : 'en'
}

const i18n = createI18n({
  legacy: false, // 使用 Composition API 模式
  locale: getDefaultLocale(),
  fallbackLocale: 'zh',
  messages: {
    zh,
    en
  }
})

export default i18n

// 导出支持的语言列表
export const supportedLocales = ['zh', 'en']

// 切换语言的函数
export function setLocale(locale) {
  if (supportedLocales.includes(locale)) {
    i18n.global.locale.value = locale
    localStorage.setItem('locale', locale)
    document.documentElement.lang = locale
  }
}





