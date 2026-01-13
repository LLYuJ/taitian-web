<template>
  <div class="language-switcher" ref="switcherRef">
    <button class="lang-trigger" @click="toggleDropdown">
      <!-- 地球图标 -->
      <svg class="globe-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"/>
        <path d="M2 12h20"/>
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
      </svg>
      <span class="current-lang">{{ currentLanguageLabel }}</span>
      <svg class="arrow-icon" :class="{ 'open': isOpen }" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M6 9l6 6 6-6"/>
      </svg>
    </button>
    
    <!-- 下拉菜单 -->
    <div class="dropdown-menu" v-show="isOpen">
      <button
        v-for="lang in languages"
        :key="lang.code"
        :class="['dropdown-item', { active: currentLocale === lang.code }]"
        @click="selectLanguage(lang.code)"
      >
        {{ lang.label }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useLocale } from '@/composables/useLocale'

const { currentLocale, switchLocale } = useLocale()

const isOpen = ref(false)
const switcherRef = ref(null)

const languages = [
  { code: 'zh', label: '中文' },
  { code: 'en', label: 'English' }
]

const currentLanguageLabel = computed(() => {
  const lang = languages.find(l => l.code === currentLocale.value)
  return lang ? lang.label : '中文'
})

const toggleDropdown = () => {
  isOpen.value = !isOpen.value
}

const selectLanguage = (code) => {
  switchLocale(code)
  isOpen.value = false
}

// 点击外部关闭下拉菜单
const handleClickOutside = (event) => {
  if (switcherRef.value && !switcherRef.value.contains(event.target)) {
    isOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style lang="scss" scoped>
.language-switcher {
  position: relative;
  
  .lang-trigger {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 6px 10px;
    border: none;
    background: transparent;
    color: #333;
    font-size: 14px;
    cursor: pointer;
    border-radius: 4px;
    transition: all 0.3s;
    
    &:hover {
      color: #2CB5BE;
    }
    
    .globe-icon {
      width: 18px;
      height: 18px;
    }
    
    .current-lang {
      font-weight: 500;
    }
    
    .arrow-icon {
      width: 14px;
      height: 14px;
      transition: transform 0.3s;
      opacity: 0.6;
      
      &.open {
        transform: rotate(180deg);
      }
    }
  }
  
  .dropdown-menu {
    position: absolute;
    top: 100%;
    right: 0;
    margin-top: 4px;
    background: white;
    border-radius: 6px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
    min-width: 100px;
    overflow: hidden;
    z-index: 1000;
    
    .dropdown-item {
      display: block;
      width: 100%;
      padding: 10px 16px;
      border: none;
      background: transparent;
      color: #333;
      font-size: 14px;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
      
      &:hover {
        background: #f5f5f5;
        color: #2CB5BE;
      }
      
      &.active {
        background: #2CB5BE;
        color: white;
      }
    }
  }
}
</style>
