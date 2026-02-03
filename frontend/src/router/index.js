import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import i18n, { supportedLocales, setLocale } from '@/i18n'

// 主要页面路由（带语言前缀）
const mainRoutes = [
  // 首页
  {
    path: '',
    name: 'Home',
    component: () => import('@/views/Home.vue')
  },
  
  // 关于泰田
  {
    path: 'about',
    name: 'About',
    component: () => import('@/views/About.vue')
  },
  {
    path: 'about/overview',
    name: 'AboutOverview',
    component: () => import('@/views/About.vue')
  },
  {
    path: 'about/production',
    name: 'AboutProduction',
    component: () => import('@/views/About.vue')
  },
  {
    path: 'about/honors',
    name: 'AboutHonors',
    component: () => import('@/views/About.vue')
  },
  
  // 产品中心
  {
    path: 'products',
    name: 'Products',
    component: () => import('@/views/Products.vue')
  },
  {
    path: 'products/precision-machine',
    name: 'ProductsPrecisionMachine',
    component: () => import('@/views/Products.vue')
  },
  {
    path: 'products/screw-compressor',
    name: 'ProductsScrewCompressor',
    component: () => import('@/views/Products.vue')
  },
  {
    path: 'products/screw-compressor/:subType',
    name: 'ProductsScrewCompressorDetail',
    component: () => import('@/views/Products.vue')
  },
  {
    path: 'products/compressor-host',
    name: 'ProductsCompressorHost',
    component: () => import('@/views/Products.vue')
  },
  {
    path: 'products/compressor-host/:subType',
    name: 'ProductsCompressorHostDetail',
    component: () => import('@/views/Products.vue')
  },
  {
    path: 'products/electric-tools',
    name: 'ProductsElectricTools',
    component: () => import('@/views/Products.vue')
  },
  {
    path: 'products/electric-tools/:subType',
    name: 'ProductsElectricToolsDetail',
    component: () => import('@/views/Products.vue')
  },
  {
    path: 'products/pneumatic-tools',
    name: 'ProductsPneumaticTools',
    component: () => import('@/views/Products.vue')
  },
  {
    path: 'products/pneumatic-tools/:subType',
    name: 'ProductsPneumaticToolsDetail',
    component: () => import('@/views/Products.vue')
  },
  {
    path: 'products/lubrication',
    name: 'ProductsLubrication',
    component: () => import('@/views/Products.vue')
  },
  {
    path: 'products/lubrication/:subType',
    name: 'ProductsLubricationDetail',
    component: () => import('@/views/Products.vue')
  },
  
  // 服务支持
  {
    path: 'services',
    name: 'Services',
    component: () => import('@/views/Services.vue')
  },
  {
    path: 'services/pre-sales',
    name: 'ServicesPreSales',
    component: () => import('@/views/Services.vue')
  },
  {
    path: 'services/after-sales',
    name: 'ServicesAfterSales',
    component: () => import('@/views/Services.vue')
  },
  {
    path: 'services/documents',
    name: 'ServicesDocuments',
    component: () => import('@/views/Services.vue')
  },
  
  // 创新研发
  {
    path: 'research',
    name: 'Research',
    component: () => import('@/views/Applications.vue')
  },
  {
    path: 'research/tech-center',
    name: 'ResearchTechCenter',
    component: () => import('@/views/Applications.vue')
  },
  {
    path: 'research/patents',
    name: 'ResearchPatents',
    component: () => import('@/views/Applications.vue')
  },
  
  // 新闻资讯
  {
    path: 'news',
    name: 'News',
    component: () => import('@/views/News.vue')
  },
  {
    path: 'news/company',
    name: 'NewsCompany',
    component: () => import('@/views/News.vue')
  },
  {
    path: 'news/exhibitions',
    name: 'NewsExhibitions',
    component: () => import('@/views/News.vue')
  },
  {
    path: 'news/detail/:id',
    name: 'NewsDetail',
    component: () => import('@/views/NewsDetail.vue')
  },
  
  // 联系我们
  {
    path: 'contact',
    name: 'Contact',
    component: () => import('@/views/Contact.vue')
  },
  
  // 行业应用（保留旧路由兼容）
  {
    path: 'applications',
    name: 'Applications',
    component: () => import('@/views/Applications.vue')
  }
]

// 生成带语言前缀的路由
function createLocaleRoutes() {
  return supportedLocales.map(locale => ({
    path: `/${locale}`,
    component: () => import('@/layouts/MainLayout.vue'),
    children: mainRoutes.map(route => ({
      ...route,
      name: `${route.name}-${locale}`,
      meta: { ...route.meta, locale }
    }))
  }))
}

const router = createRouter({
  history: createWebHistory(),
  routes: [
    // 带语言前缀的主路由
    ...createLocaleRoutes(),
    
    // 管理后台路由（不带语言前缀）
    {
      path: '/admin',
      component: () => import('@/layouts/AdminLayout.vue'),
      meta: { requiresAuth: true },
      children: [
        {
          path: '',
          name: 'AdminDashboard',
          component: () => import('@/views/admin/Dashboard.vue')
        },
        {
          path: 'media',
          name: 'AdminMedia',
          component: () => import('@/views/admin/MediaManagement.vue')
        },
        {
          path: 'news',
          name: 'AdminNews',
          component: () => import('@/views/admin/NewsManagement.vue')
        }
      ]
    },
    
    // 登录页面（不带语言前缀）
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/views/Login.vue')
    },
    
    // 根路径重定向到默认语言
    {
      path: '/',
      redirect: () => {
        const savedLocale = localStorage.getItem('locale')
        if (savedLocale && supportedLocales.includes(savedLocale)) {
          return `/${savedLocale}`
        }
        const browserLang = navigator.language || navigator.userLanguage
        return browserLang.startsWith('zh') ? '/zh' : '/en'
      }
    },
    
    // 捕获所有未匹配的路由，重定向到默认语言首页
    {
      path: '/:pathMatch(.*)*',
      redirect: '/zh'
    }
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// 路由守卫
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  
  // 检查认证
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'Login', query: { redirect: to.fullPath } })
    return
  }
  
  // 同步语言设置
  const pathLocale = to.path.split('/')[1]
  if (supportedLocales.includes(pathLocale)) {
    if (i18n.global.locale.value !== pathLocale) {
      setLocale(pathLocale)
    }
  }
  
  next()
})

export default router
