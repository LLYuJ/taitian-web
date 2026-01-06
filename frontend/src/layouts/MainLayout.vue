<template>
  <div class="main-layout">
    <header class="header">
      <div class="container header-content">
        <div class="logo">
          <router-link :to="localePath('/')">
            <img src="@/assets/images/logos/logo_blue.png" alt="泰田集团" class="logo-img" />
          </router-link>
        </div>
        
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
            
            <!-- Mega Menu 下拉面板 -->
            <div 
              v-if="menu.children?.length"
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
                        :alt="menu.key === 'products' ? t(`nav.sub.${activeCategory}`) : t(`nav.${menu.key}`)" 
                      />
                    </div>
                    <p class="promo-text">{{ t('nav.promoText') }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </nav>
        
        <div class="header-actions">
          <LanguageSwitcher />
          <router-link to="/admin" class="admin-link">{{ t('nav.admin') }}</router-link>
        </div>
      </div>
    </header>

    <main class="main-content">
      <router-view />
    </main>

    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-section">
            <h3>{{ t('footer.contactUs') }}</h3>
            <p>{{ t('footer.serviceLine') }}</p>
            <p>{{ t('footer.email') }}</p>
            <p>{{ t('footer.address') }}</p>
          </div>
          <div class="footer-section">
            <h3>{{ t('footer.quickLinks') }}</h3>
            <router-link :to="localePath('/about')">{{ t('footer.aboutUs') }}</router-link>
            <router-link :to="localePath('/products')">{{ t('nav.products') }}</router-link>
            <router-link :to="localePath('/news')">{{ t('nav.news') }}</router-link>
            <router-link :to="localePath('/contact')">{{ t('nav.contact') }}</router-link>
          </div>
          <div class="footer-section">
            <h3>{{ t('footer.followUs') }}</h3>
            <div class="qrcode-wrapper">
              <img src="@/assets/images/misc/qrcode.jpg" alt="微信公众号" class="qrcode-img" loading="lazy" />
              <p>{{ t('footer.wechat') }}</p>
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
import { useLocale } from '@/composables/useLocale'
import LanguageSwitcher from '@/components/LanguageSwitcher.vue'

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

const activeMenu = ref(null)
const activeCategory = ref(null)

// 导航菜单结构配置
const navigationMenus = [
  {
    key: 'about',
    path: '/about',
    children: [
      { key: 'overview', path: '/about/overview' },
      { key: 'production', path: '/about/production' },
      { key: 'honors', path: '/about/honors' }
    ]
  },
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
    key: 'services',
    path: '/services',
    children: [
      { key: 'preSales', path: '/services/pre-sales' },
      { key: 'afterSales', path: '/services/after-sales' },
      { key: 'documents', path: '/services/documents' }
    ]
  },
  {
    key: 'research',
    path: '/research',
    children: [
      { key: 'techCenter', path: '/research/tech-center' },
      { key: 'patents', path: '/research/patents' }
    ]
  },
  {
    key: 'news',
    path: '/news',
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
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;

  .header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 80px;
  }

  .logo {
    flex-shrink: 0;
    
    a {
      display: flex;
      align-items: center;
    }
    
    .logo-img {
      height: 50px;
      width: auto;
    }
  }

  .nav {
    display: flex;
    align-items: center;
    gap: 8px;

    .nav-item {
      color: #333;
      text-decoration: none;
      font-size: 16px;
      font-weight: 500;
      padding: 8px 16px;
      position: relative;
      transition: color 0.3s;
      display: flex;
      align-items: center;
      gap: 4px;

      // 底线伪元素 - 默认隐藏
      &::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        width: 0;
        height: 3px;
        background: #2CB5BE;
        transition: width 0.3s ease, left 0.3s ease;
      }

      // 选中状态只保持颜色，不显示底线
      &.router-link-active {
        color: #2CB5BE;
      }

      // hover 时变色并显示底线动画
      &:hover {
        color: #2CB5BE;
        
        &::after {
          width: calc(100% - 32px);
          left: 16px;
        }
      }
      
      .dropdown-icon {
        width: 14px;
        height: 14px;
        transition: transform 0.3s;
      }
    }
    
    .nav-dropdown {
      position: relative;
      
      &:hover {
        .nav-item {
          color: #2CB5BE;
          
          &::after {
            width: calc(100% - 32px);
            left: 16px;
          }
          
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
    gap: 20px;
    
    .admin-link {
      color: #666;
      text-decoration: none;
      font-size: 14px;
      
      &:hover {
        color: #2CB5BE;
      }
    }
  }
}

// Mega Menu 样式
.mega-menu {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: white;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
  border-radius: 0 0 8px 8px;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  min-width: 600px;
  
  &.active {
    opacity: 1;
    visibility: visible;
  }
  
  &.has-third-level {
    min-width: 900px;
  }
  
  .mega-menu-inner {
    padding: 0;
  }
  
  .mega-menu-header {
    padding: 16px 24px;
    border-bottom: 1px solid #eee;
    background: #fafafa;
    
    .mega-menu-title {
      font-size: 14px;
      color: #999;
      font-weight: 500;
    }
  }
  
  .mega-menu-content {
    display: flex;
    min-height: 280px;
  }
  
  // 二级分类列表
  .category-list {
    width: 200px;
    border-right: 1px solid #eee;
    padding: 12px 0;
    
    .category-item {
      .category-link {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 24px;
        color: #333;
        text-decoration: none;
        font-size: 15px;
        transition: all 0.2s;
        
        .arrow-icon {
          width: 16px;
          height: 16px;
          opacity: 0;
          transition: opacity 0.2s;
        }
        
        &:hover {
          background: #f5f5f5;
          color: #2CB5BE;
        }
      }
      
      &.active {
        .category-link {
          background: #f07c00;
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
    width: 280px;
    border-right: 1px solid #eee;
    padding: 12px 0;
    background: #fafafa;
    
    .product-items {
      display: flex;
      flex-direction: column;
    }
    
    .product-link {
      padding: 10px 24px;
      color: #555;
      text-decoration: none;
      font-size: 14px;
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
    padding: 24px;
    display: flex;
    flex-direction: column;
    
    .promo-image {
      flex: 1;
      border-radius: 8px;
      overflow: hidden;
      margin-bottom: 16px;
      
      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
    }
    
    .promo-text {
      font-size: 14px;
      color: #666;
      line-height: 1.6;
    }
  }
}

.main-content {
  flex: 1;
}

.footer {
  background: #1a1a1a;
  color: white;
  padding: 60px 0 20px;
  margin-top: 80px;

  .footer-content {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 60px;
    margin-bottom: 40px;
  }

  .footer-section {
    h3 {
      color: #2CB5BE;
      font-size: 18px;
      margin-bottom: 20px;
    }

    p, a {
      color: #ccc;
      margin: 10px 0;
      font-size: 14px;
      text-decoration: none;
      display: block;

      &:hover {
        color: #2CB5BE;
      }
    }
    
    .qrcode-wrapper {
      text-align: center;
      
      .qrcode-img {
        width: 120px;
        height: 120px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 10px;
      }
    }
  }

  .footer-bottom {
    border-top: 1px solid #333;
    padding-top: 20px;
    text-align: center;

    p {
      color: #666;
      font-size: 14px;
    }
  }
}

@media (max-width: 1200px) {
  .mega-menu {
    min-width: 500px !important;
    
    &.has-third-level {
      min-width: 700px !important;
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
      grid-template-columns: 1fr;
      gap: 30px;
    }
  }
}
</style>
