<template>
  <div class="main-layout">
    <!-- 联系弹窗（联系我们页面不显示） -->
    <ContactPopup v-if="!isContactPage" />
    
    <header class="header">
      <div class="wide-container header-content">
        <!-- 左侧 Logo 区域 -->
        <div class="logo-area">
          <router-link :to="localePath('/')" class="logo-link">
            <img src="@/assets/images/logos/logo_blue.png" alt="泰田集团" class="logo-img" />
          </router-link>
        </div>
        
        <!-- 右侧导航区域 -->
        <div class="nav-area">
          <nav class="nav">
            <!-- 首页 -->
            <router-link :to="localePath('/')" class="nav-item">{{ t('nav.home') }}</router-link>
            
            <!-- 带下拉菜单的导航项 -->
            <div 
              v-for="menu in navigationMenus" 
              :key="menu.key"
              class="nav-dropdown"
              @mouseenter="handleMenuEnter(menu)"
              @mouseleave="handleMenuLeave"
            >
              <router-link 
                :to="localePath(menu.path)" 
                class="nav-item"
                :class="{ 'has-submenu': menu.children?.length }"
              >
                {{ t(`nav.${menu.key}`) }}
                <svg v-if="menu.children?.length" class="dropdown-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </router-link>
              
              <!-- 简洁下拉菜单 (关于泰田、服务支持、创新研发、新闻资讯) -->
              <div 
                v-if="menu.children?.length && menu.isSimple"
                class="simple-dropdown"
                :class="{ 'active': activeMenu === menu.key }"
              >
                <router-link 
                  v-for="child in menu.children"
                  :key="child.key"
                  :to="localePath(child.path)"
                  class="simple-dropdown-link"
                  @click="closeMenu"
                >
                  {{ t(`nav.sub.${child.key}`) }}
                </router-link>
              </div>
              
              <!-- Mega Menu 下拉面板 (产品中心) -->
              <div 
                v-if="menu.children?.length && !menu.isSimple"
                class="mega-menu"
                :class="{ 'active': activeMenu === menu.key, 'has-third-level': menu.hasThirdLevel }"
              >
                <div class="mega-menu-inner">
                  <!-- 二级菜单标题 -->
                  <div class="mega-menu-header">
                    <span class="mega-menu-title">{{ t(`nav.${menu.key}`) }}</span>
                  </div>
                  
                  <div class="mega-menu-content">
                    <!-- 二级菜单列表 -->
                    <div class="category-list">
                      <div 
                        v-for="child in menu.children" 
                        :key="child.key"
                        class="category-item"
                        :class="{ 'active': activeCategory === child.key, 'has-children': child.children?.length }"
                        @mouseenter="activeCategory = child.key"
                      >
                        <router-link 
                          :to="localePath(child.path)"
                          class="category-link"
                          @click="closeMenu"
                        >
                          {{ t(`nav.sub.${child.key}`) }}
                          <svg v-if="child.children?.length" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                          </svg>
                        </router-link>
                      </div>
                    </div>
                    
                    <!-- 三级菜单列表 (仅产品中心有) -->
                    <div v-if="menu.hasThirdLevel" class="product-list">
                      <template v-for="child in menu.children" :key="child.key">
                        <div 
                          v-if="child.children?.length && activeCategory === child.key"
                          class="product-items"
                        >
                          <router-link 
                            v-for="product in child.children"
                            :key="product.key"
                            :to="localePath(product.path)"
                            class="product-link"
                            @click="closeMenu"
                          >
                            {{ t(`nav.productItems.${product.key}`) }}
                          </router-link>
                        </div>
                      </template>
                    </div>
                    
                    <!-- 右侧推荐区域 -->
                    <div class="promo-area">
                      <div class="promo-image">
                        <img 
                          :src="menu.key === 'products' ? getProductImage(activeCategory) : getPromoImage(menu.key)" 
                          :alt="menu.key === 'products' && activeCategory ? t(`nav.sub.${activeCategory}`) : t(`nav.${menu.key}`)" 
                        />
                      </div>
                      <p class="promo-text">{{ t('nav.promoText') }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </nav>
          
          <!-- 右侧功能按钮 -->
          <div class="header-actions">
            <!-- 搜索按钮 -->
            <button class="search-btn" @click="handleSearchClick">
              <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8"/>
                <path d="M21 21l-4.35-4.35"/>
              </svg>
            </button>
            <span class="divider">|</span>
            <LanguageSwitcher />
          </div>
        </div>
      </div>
    </header>

    <main class="main-content">
      <router-view />
    </main>

    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <!-- 产品中心 -->
          <div class="footer-section">
            <h3>{{ t('footer.productCenter') }}</h3>
            <router-link :to="localePath('/products/precision-machine')">{{ t('footer.precisionMachine') }}</router-link>
            <router-link :to="localePath('/products/screw-compressor')">{{ t('footer.screwCompressor') }}</router-link>
            <router-link :to="localePath('/products/compressor-host')">{{ t('footer.compressorHost') }}</router-link>
            <router-link :to="localePath('/products/electric-tools')">{{ t('footer.electricTools') }}</router-link>
            <router-link :to="localePath('/products/pneumatic-tools')">{{ t('footer.pneumaticTools') }}</router-link>
            <router-link :to="localePath('/products/lubrication')">{{ t('footer.lubricationEquipment') }}</router-link>
          </div>
          <!-- 服务支持 -->
          <div class="footer-section">
            <h3>{{ t('footer.serviceSupport') }}</h3>
            <router-link :to="localePath('/services/pre-sales')">{{ t('footer.preSales') }}</router-link>
            <router-link :to="localePath('/services/after-sales')">{{ t('footer.afterSales') }}</router-link>
            <router-link :to="localePath('/services/documents')">{{ t('footer.documents') }}</router-link>
          </div>
          <!-- 联系我们 -->
          <div class="footer-section contact-section">
            <h3>{{ t('footer.contactUs') }}</h3>
            <p><span class="label">{{ t('footer.companyAddress') }}</span>{{ t('footer.addressValue') }}</p>
            <p><span class="label">{{ t('footer.phone') }}</span>{{ t('footer.phoneValue') }}</p>
            <p><span class="label">{{ t('footer.wechatLabel') }}</span>{{ t('footer.wechatValue') }}</p>
            <p><span class="label">{{ t('footer.emailLabel') }}</span>{{ t('footer.emailValue') }}</p>
          </div>
          <!-- 关注我们 -->
          <div class="footer-section follow-section">
            <h3>{{ t('footer.followUs') }}</h3>
            <div class="qrcode-row">
              <div class="qrcode-item">
                <img src="@/assets/images/misc/qrcode.jpg" alt="微信视频号" class="qrcode-img" loading="lazy" />
                <p>{{ t('footer.wechatVideo') }}</p>
              </div>
              <div class="qrcode-item">
                <img src="@/assets/images/misc/qrcode.jpg" alt="抖音号" class="qrcode-img" loading="lazy" />
                <p>{{ t('footer.douyin') }}</p>
              </div>
              <div class="qrcode-item">
                <img src="@/assets/images/misc/qrcode.jpg" alt="阿里巴巴国际站" class="qrcode-img" loading="lazy" />
                <p>{{ t('footer.alibaba') }}</p>
              </div>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p>{{ t('footer.copyright') }}</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useLocale } from '@/composables/useLocale'
import LanguageSwitcher from '@/components/LanguageSwitcher.vue'
import ContactPopup from '@/components/ContactPopup.vue'

// 导入推荐区图片
import productAllImg from '@/assets/images/banners/product-all.jpg'

// 导入产品图片
import precisionMachineImg from '@/assets/images/products/precision-machine.png'
import screwCompressorImg from '@/assets/images/products/screw-compressor.jpg'
import compressorHostImg from '@/assets/images/products/compressor-host.jpg'
import electricToolsImg from '@/assets/images/products/industrial-wrench.jpg'
import pneumaticToolsImg from '@/assets/images/products/auto-repair-tools.png'
import lubricationEquipmentImg from '@/assets/images/products/lubrication-equipment.jpg'

const { t, localePath } = useLocale()
const route = useRoute()

// 检查是否在联系我们页面
const isContactPage = computed(() => {
  return route.path.includes('/contact')
})

const activeMenu = ref(null)
const activeCategory = ref(null)

// 导航菜单结构配置 - 顺序：首页、产品中心、关于泰田、服务支持、创新研发、新闻资讯、联系我们
const navigationMenus = [
  {
    key: 'products',
    path: '/products',
    hasThirdLevel: true,
    children: [
      { key: 'precisionMachine', path: '/products/precision-machine' },
      { 
        key: 'screwCompressor', 
        path: '/products/screw-compressor',
        children: [
          { key: 'singleStage', path: '/products/screw-compressor/single-stage' },
          { key: 'verticalDualStage', path: '/products/screw-compressor/vertical-dual-stage' },
          { key: 'horizontalDualStage', path: '/products/screw-compressor/horizontal-dual-stage' },
          { key: 'portable', path: '/products/screw-compressor/portable' }
        ]
      },
      { 
        key: 'compressorHost', 
        path: '/products/compressor-host',
        children: [
          { key: 'singleStageHost', path: '/products/compressor-host/single-stage' },
          { key: 'verticalDualStageHost', path: '/products/compressor-host/vertical-dual-stage' },
          { key: 'horizontalDualStageHost', path: '/products/compressor-host/horizontal-dual-stage' }
        ]
      },
      { 
        key: 'electricTools', 
        path: '/products/electric-tools',
        children: [
          { key: 'batteryImpact', path: '/products/electric-tools/battery-impact' },
          { key: 'batteryClutch', path: '/products/electric-tools/battery-clutch' },
          { key: 'batterySensor', path: '/products/electric-tools/battery-sensor' }
        ]
      },
      { 
        key: 'pneumaticTools', 
        path: '/products/pneumatic-tools',
        children: [
          { key: 'autoRepairImpact', path: '/products/pneumatic-tools/auto-repair' },
          { key: 'industrialImpact', path: '/products/pneumatic-tools/industrial' }
        ]
      },
      { 
        key: 'lubricationEquipment', 
        path: '/products/lubrication',
        children: [
          { key: 'greaseMachine', path: '/products/lubrication/grease' },
          { key: 'oilMachine', path: '/products/lubrication/oil' }
        ]
      }
    ]
  },
  {
    key: 'about',
    path: '/about',
    isSimple: true,
    children: [
      { key: 'overview', path: '/about/overview' },
      { key: 'production', path: '/about/production' },
      { key: 'honors', path: '/about/honors' }
    ]
  },
  {
    key: 'services',
    path: '/services',
    isSimple: true,
    children: [
      { key: 'preSales', path: '/services/pre-sales' },
      { key: 'afterSales', path: '/services/after-sales' },
      { key: 'documents', path: '/services/documents' }
    ]
  },
  {
    key: 'research',
    path: '/research',
    isSimple: true,
    children: [
      { key: 'techCenter', path: '/research/tech-center' },
      { key: 'patents', path: '/research/patents' }
    ]
  },
  {
    key: 'news',
    path: '/news',
    isSimple: true,
    children: [
      { key: 'companyNews', path: '/news/company' },
      { key: 'exhibitions', path: '/news/exhibitions' }
    ]
  },
  {
    key: 'contact',
    path: '/contact',
    children: []
  }
]

// 搜索按钮点击（暂时无功能）
const handleSearchClick = () => {
  // 暂时不做任何处理
  console.log('Search clicked')
}

// 获取推荐区域图片（非产品菜单使用统一图片）
const getPromoImage = () => {
  return productAllImg
}

// 获取产品分类图片
const getProductImage = (categoryKey) => {
  const productImages = {
    precisionMachine: precisionMachineImg,
    screwCompressor: screwCompressorImg,
    compressorHost: compressorHostImg,
    electricTools: electricToolsImg,
    pneumaticTools: pneumaticToolsImg,
    lubricationEquipment: lubricationEquipmentImg
  }
  return productImages[categoryKey] || precisionMachineImg
}

// 处理菜单进入
const handleMenuEnter = (menu) => {
  activeMenu.value = menu.key
  // 如果是产品中心，设置默认选中第一个分类
  if (menu.key === 'products' && menu.children?.length > 0) {
    activeCategory.value = menu.children[0].key
  }
}

// 处理菜单离开
const handleMenuLeave = () => {
  activeMenu.value = null
  activeCategory.value = null
}

// 关闭菜单
const closeMenu = () => {
  activeMenu.value = null
  activeCategory.value = null
}
</script>

<style lang="scss" scoped>
.main-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  background: white;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
  position: sticky;
  top: 0;
  z-index: 1000;
  border-bottom: 1px solid #eee;

  .header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 60px;
    position: relative; // 作为 mega-menu 的定位参考
  }

  // 左侧 Logo 区域
  .logo-area {
    display: flex;
    align-items: center;
    flex-shrink: 0;
    
    .logo-link {
      display: flex;
      align-items: center;
    }
    
    .logo-img {
      height: 36px;
      width: auto;
    }
  }

  // 右侧导航区域
  .nav-area {
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .nav {
    display: flex;
    align-items: center;
    gap: 0;

    .nav-item {
      color: #333;
      text-decoration: none;
      font-size: 15px;
      font-weight: 500;
      padding: 8px 14px;
      position: relative;
      transition: color 0.3s;
      display: flex;
      align-items: center;
      gap: 4px;
      white-space: nowrap;

      // 选中状态 - 使用主题色
      &.router-link-active {
        color: #2CB5BE;
      }

      // hover 时变色
      &:hover {
        color: #2CB5BE;
      }
      
      .dropdown-icon {
        width: 12px;
        height: 12px;
        transition: transform 0.3s;
        opacity: 0.6;
      }
    }
    
    .nav-dropdown {
      position: relative; // 简洁下拉菜单相对于此定位
      
      &:hover {
        .nav-item {
          color: #2CB5BE;
          
          .dropdown-icon {
            transform: rotate(180deg);
          }
        }
      }
    }
  }

  .header-actions {
    display: flex;
    align-items: center;
    gap: 12px;
    
    .search-btn {
      background: none;
      border: none;
      cursor: pointer;
      padding: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      
      .search-icon {
        width: 18px;
        height: 18px;
        color: #333;
        transition: color 0.3s;
      }
      
      &:hover .search-icon {
        color: #2CB5BE;
      }
    }
    
    .divider {
      color: #ddd;
      font-size: 14px;
    }
  }
}

// 简洁下拉菜单样式
.simple-dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  background: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-top: 1px solid #eee;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 999;
  min-width: 120px;
  padding: 8px 0;
  border-radius: 0 0 4px 4px;
  
  &.active {
    opacity: 1;
    visibility: visible;
  }
  
  .simple-dropdown-link {
    display: block;
    padding: 10px 14px;
    color: #333;
    text-decoration: none;
    font-size: 14px;
    white-space: nowrap;
    transition: all 0.2s;
    
    &:hover {
      background: rgba(44, 181, 190, 0.1);
      color: #2CB5BE;
    }
  }
}

// Mega Menu 样式
.mega-menu {
  position: fixed;
  top: 60px; // 和 header 高度一致，紧贴 header 底部
  left: 50%;
  transform: translateX(-50%);
  background: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-top: 1px solid #eee; // 顶部横线与标题栏底部横线平行
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 999;
  width: 620px; // 适当减小宽度
  
  &.active {
    opacity: 1;
    visibility: visible;
  }
  
  &.has-third-level {
    width: 780px;
  }
  
  .mega-menu-inner {
    width: 100%;
    padding: 0 20px;
  }
  
  .mega-menu-header {
    padding: 10px 0;
    border-bottom: 1px solid #eee;
    
    .mega-menu-title {
      font-size: 13px;
      color: #999;
      font-weight: 500;
    }
  }
  
  .mega-menu-content {
    display: flex;
    min-height: 200px;
  }
  
  // 二级分类列表
  .category-list {
    width: 160px;
    border-right: 1px solid #eee;
    padding: 8px 0;
    
    .category-item {
      .category-link {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 8px 16px;
        color: #333;
        text-decoration: none;
        font-size: 14px;
        transition: all 0.2s;
        
        .arrow-icon {
          width: 14px;
          height: 14px;
          opacity: 0;
          transition: opacity 0.2s;
        }
        
        &:hover {
          background: rgba(44, 181, 190, 0.1);
          color: #2CB5BE;
        }
      }
      
      &.active {
        .category-link {
          background: #2CB5BE;
          color: white;
          
          .arrow-icon {
            opacity: 1;
          }
        }
      }
      
      &.has-children {
        .category-link .arrow-icon {
          opacity: 0.5;
        }
        
        &.active .category-link .arrow-icon {
          opacity: 1;
        }
      }
    }
  }
  
  // 三级产品列表
  .product-list {
    width: 180px;
    border-right: 1px solid #eee;
    padding: 8px 0;
    background: #fafafa;
    
    .product-items {
      display: flex;
      flex-direction: column;
    }
    
    .product-link {
      padding: 8px 16px;
      color: #555;
      text-decoration: none;
      font-size: 13px;
      transition: all 0.2s;
      
      &:hover {
        background: #eee;
        color: #2CB5BE;
      }
    }
  }
  
  // 推荐区域
  .promo-area {
    flex: 1;
    padding: 16px;
    display: flex;
    flex-direction: column;
    max-width: 380px;
    
    .promo-image {
      flex: 1;
      border-radius: 6px;
      overflow: hidden;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #f9f9f9; // 浅灰背景，防止图片留白不协调
      
      img {
        max-width: 100%;
        max-height: 180px;
        width: auto;
        height: auto;
        object-fit: contain; // 保持图片完整显示
      }
    }
    
    .promo-text {
      font-size: 12px;
      color: #666;
      line-height: 1.5;
    }
  }
}

.main-content {
  flex: 1;
}

.footer {
  background: #000000;
  color: #ffffff;
  padding: 60px 0 20px;
  margin-top: 80px;

  .footer-content {
    display: grid;
    grid-template-columns: 1fr 1fr 1.2fr 1.5fr;
    gap: 40px;
    margin-bottom: 40px;
  }

  .footer-section {
    h3 {
      color: #ffffff;
      font-size: 18px;
      font-weight: 600;
      margin-bottom: 24px;
      position: relative;
    }

    p, a {
      color: #ffffff;
      margin: 12px 0;
      font-size: 14px;
      text-decoration: none;
      display: block;
      line-height: 1.6;
      transition: color 0.3s ease;

      &:hover {
        color: #2CB5BE;
      }
    }
    
    &.contact-section {
      p {
        .label {
          color: #ffffff;
          font-weight: 500;
        }
      }
    }
    
    &.follow-section {
      .qrcode-row {
        display: flex;
        gap: 20px;
        
        .qrcode-item {
          text-align: center;
          
          .qrcode-img {
            width: 100px;
            height: 100px;
            object-fit: cover;
            border-radius: 6px;
            margin-bottom: 8px;
            border: 1px solid #333;
          }
          
          p {
            font-size: 12px;
            color: #ffffff;
            margin: 0;
            
            &:hover {
              color: #2CB5BE;
            }
          }
        }
      }
    }
  }

  .footer-bottom {
    border-top: 1px solid #333;
    padding-top: 20px;
    text-align: center;

    p {
      color: #cccccc;
      font-size: 13px;
    }
  }
}

@media (max-width: 1200px) {
  .mega-menu {
    width: 520px !important;
    
    &.has-third-level {
      width: 680px !important;
    }
    
    .promo-area {
      display: none;
    }
  }
}

@media (max-width: 768px) {
  .header {
    .header-content {
      flex-wrap: wrap;
      height: auto;
      padding: 15px 0;
    }

    .nav {
      width: 100%;
      flex-wrap: wrap;
      gap: 8px;
      
      .nav-dropdown {
        .mega-menu {
          position: fixed;
          left: 0;
          right: 0;
          transform: none;
          min-width: 100% !important;
          border-radius: 0;
          
          .mega-menu-content {
            flex-direction: column;
          }
          
          .category-list,
          .product-list {
            width: 100%;
            border-right: none;
            border-bottom: 1px solid #eee;
          }
        }
      }
    }
  }

  .footer {
    .footer-content {
      grid-template-columns: 1fr 1fr;
      gap: 30px;
    }
    
    .footer-section.follow-section {
      grid-column: span 2;
      
      .qrcode-row {
        justify-content: flex-start;
      }
    }
  }
}

@media (max-width: 576px) {
  .footer {
    .footer-content {
      grid-template-columns: 1fr;
      gap: 24px;
    }
    
    .footer-section.follow-section {
      grid-column: span 1;
      
      .qrcode-row {
        justify-content: center;
        flex-wrap: wrap;
      }
    }
  }
}
</style>
