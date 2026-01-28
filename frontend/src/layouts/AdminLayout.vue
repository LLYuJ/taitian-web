<template>
  <div class="admin-layout">
    <aside class="sidebar">
      <div class="sidebar-header">
        <h2>管理后台</h2>
      </div>
      <nav class="sidebar-nav">
        <router-link to="/admin" class="nav-item" exact>
          <el-icon><Grid /></el-icon>
          <span>仪表盘</span>
        </router-link>
        <router-link to="/admin/news" class="nav-item">
          <el-icon><Document /></el-icon>
          <span>新闻管理</span>
        </router-link>
        <router-link to="/admin/media" class="nav-item">
          <el-icon><Picture /></el-icon>
          <span>媒体管理</span>
        </router-link>
      </nav>
      <div class="sidebar-footer">
        <el-button @click="handleLogout" type="danger" plain>
          <el-icon><SwitchButton /></el-icon>
          退出登录
        </el-button>
      </div>
    </aside>

    <div class="main-area">
      <header class="admin-header">
        <div class="header-content">
          <h1>泰田集团管理系统</h1>
          <div class="header-actions">
            <router-link to="/" class="back-home">
              <el-icon><HomeFilled /></el-icon>
              返回前台
            </router-link>
          </div>
        </div>
      </header>

      <main class="admin-content">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { ElMessage } from 'element-plus'
import { Grid, Document, Picture, SwitchButton, HomeFilled } from '@element-plus/icons-vue'

const router = useRouter()
const authStore = useAuthStore()

const handleLogout = () => {
  authStore.logout()
  ElMessage.success('已退出登录')
  router.push('/login')
}
</script>

<style lang="scss" scoped>
.admin-layout {
  display: flex;
  min-height: 100vh;
  background: #f0f2f5;
}

.sidebar {
  width: 250px;
  background: #001529;
  display: flex;
  flex-direction: column;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;

  .sidebar-header {
    padding: 24px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);

    h2 {
      color: white;
      font-size: 20px;
      margin: 0;
      text-align: center;
    }
  }

  .sidebar-nav {
    flex: 1;
    padding: 20px 0;

    .nav-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 14px 24px;
      color: rgba(255, 255, 255, 0.7);
      text-decoration: none;
      transition: all 0.3s;

      .el-icon {
        font-size: 18px;
      }

      &:hover {
        color: white;
        background: rgba(255, 255, 255, 0.1);
      }

      &.router-link-active {
        color: white;
        background: #2CB5BE;
      }
    }
  }

  .sidebar-footer {
    padding: 20px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);

    .el-button {
      width: 100%;
    }
  }
}

.main-area {
  flex: 1;
  margin-left: 250px;
  display: flex;
  flex-direction: column;
}

.admin-header {
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  position: sticky;
  top: 0;
  z-index: 999;

  .header-content {
    padding: 0 24px;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: space-between;

    h1 {
      font-size: 20px;
      margin: 0;
      color: #333;
    }

    .back-home {
      color: #666;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: color 0.3s;

      &:hover {
        color: #2CB5BE;
      }
    }
  }
}

.admin-content {
  flex: 1;
  padding: 24px;
}
</style>

