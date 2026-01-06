<template>
  <div class="language-switcher">
    <button
      v-for="lang in languages"
      :key="lang.code"
      :class="['lang-btn', { active: currentLocale === lang.code }]"
      @click="switchLocale(lang.code)"
    >
      {{ lang.label }}
    </button>
  </div>
</template>

<script setup>
import { useLocale } from '@/composables/useLocale'

const { currentLocale, switchLocale } = useLocale()

const languages = [
  { code: 'zh', label: '中文' },
  { code: 'en', label: 'EN' }
]
</script>

<style lang="scss" scoped>
.language-switcher {
  display: flex;
  align-items: center;
  gap: 4px;
  
  .lang-btn {
    padding: 6px 12px;
    border: none;
    background: transparent;
    color: #666;
    font-size: 14px;
    cursor: pointer;
    border-radius: 4px;
    transition: all 0.3s;
    font-weight: 500;
    
    &:hover {
      color: #2CB5BE;
      background: rgba(44, 181, 190, 0.1);
    }
    
    &.active {
      color: white;
      background: #2CB5BE;
    }
  }
}
</style>



