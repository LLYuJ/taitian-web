<template>
  <Transition name="popup">
    <div v-if="isVisible" class="contact-popup">
      <div class="popup-content">
        <router-link :to="contactPath" class="popup-left" @click="close">
          <svg class="chevron-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
          <span class="popup-text">{{ t('nav.contact') }}</span>
        </router-link>
        <router-link :to="contactPath" class="popup-btn" @click="close">
          <svg class="phone-icon" viewBox="0 0 24 24" fill="currentColor">
            <path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>
          </svg>
          400-826-1128
        </router-link>
        <button class="close-btn" @click.stop="close">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useLocale } from '@/composables/useLocale'

const route = useRoute()
const { t, localePath } = useLocale()

const isVisible = ref(true)
const isClosed = ref(false)

// 根据当前路由语言生成联系页面路径
const contactPath = computed(() => {
  return localePath('/contact')
})

const close = () => {
  isVisible.value = false
  isClosed.value = true
}

// 监听路由变化，如果之前关闭过，在路由变化时重新显示
watch(() => route.path, (newPath, oldPath) => {
  if (isClosed.value && newPath !== oldPath) {
    isVisible.value = true
    isClosed.value = false
  }
})
</script>

<style lang="scss" scoped>
.contact-popup {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1001;
  
  .popup-content {
    display: flex;
    align-items: center;
    background: #2d3436;
    border-radius: 50px;
    padding: 8px 8px 8px 16px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    gap: 16px;
  }
  
  .popup-left {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #fff;
    text-decoration: none;
    cursor: pointer;
    transition: opacity 0.3s;
    
    &:hover {
      opacity: 0.85;
    }
    
    .chevron-icon {
      width: 16px;
      height: 16px;
      opacity: 0.8;
    }
    
    .popup-text {
      font-size: 14px;
      font-weight: 500;
      white-space: nowrap;
    }
  }
  
  .popup-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    background: #2CB5BE;
    color: #fff;
    border: none;
    border-radius: 50px;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    transition: all 0.3s ease;
    white-space: nowrap;
    
    .phone-icon {
      width: 16px;
      height: 16px;
    }
    
    &:hover {
      background: #25a0a8;
      transform: scale(1.02);
    }
  }
  
  .close-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    background: transparent;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-left: -4px;
    
    svg {
      width: 14px;
      height: 14px;
      color: rgba(255, 255, 255, 0.7);
    }
    
    &:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.5);
      
      svg {
        color: #fff;
      }
    }
  }
}

// 动画
.popup-enter-active,
.popup-leave-active {
  transition: all 0.3s ease;
}

.popup-enter-from,
.popup-leave-to {
  opacity: 0;
  transform: translateX(-50%) translateY(20px);
}

// 响应式
@media (max-width: 480px) {
  .contact-popup {
    bottom: 16px;
    left: 16px;
    right: 16px;
    transform: none;
    
    .popup-content {
      width: 100%;
      justify-content: space-between;
    }
  }
  
  .popup-enter-from,
  .popup-leave-to {
    transform: translateY(20px);
  }
}
</style>
