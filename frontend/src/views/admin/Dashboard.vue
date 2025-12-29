<template>
  <div class="dashboard">
    <div class="page-title">
      <h1>仪表盘</h1>
      <p>欢迎回来，管理员</p>
    </div>

    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon" style="background: #2CB5BE;">
          <el-icon><Picture /></el-icon>
        </div>
        <div class="stat-content">
          <div class="stat-value">0</div>
          <div class="stat-label">媒体文件</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon" style="background: #52c41a;">
          <el-icon><Document /></el-icon>
        </div>
        <div class="stat-content">
          <div class="stat-value">0</div>
          <div class="stat-label">文档文件</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon" style="background: #faad14;">
          <el-icon><View /></el-icon>
        </div>
        <div class="stat-content">
          <div class="stat-value">0</div>
          <div class="stat-label">总访问量</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon" style="background: #f5222d;">
          <el-icon><User /></el-icon>
        </div>
        <div class="stat-content">
          <div class="stat-value">1</div>
          <div class="stat-label">管理员</div>
        </div>
      </div>
    </div>

    <div class="quick-actions">
      <h2>快速操作</h2>
      <div class="actions-grid">
        <router-link to="/admin/media" class="action-card">
          <el-icon><Upload /></el-icon>
          <span>上传文件</span>
        </router-link>
        
        <router-link to="/admin/media" class="action-card">
          <el-icon><FolderOpened /></el-icon>
          <span>媒体管理</span>
        </router-link>
        
        <router-link to="/" class="action-card">
          <el-icon><View /></el-icon>
          <span>预览网站</span>
        </router-link>
      </div>
    </div>

    <div class="system-info">
      <h2>系统信息</h2>
      <div class="info-card">
        <div class="info-item">
          <span class="info-label">系统版本：</span>
          <span class="info-value">v1.0.0</span>
        </div>
        <div class="info-item">
          <span class="info-label">前端框架：</span>
          <span class="info-value">Vue 3 + Vite</span>
        </div>
        <div class="info-item">
          <span class="info-label">后端框架：</span>
          <span class="info-value">FastAPI</span>
        </div>
        <div class="info-item">
          <span class="info-label">UI框架：</span>
          <span class="info-value">Element Plus</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style lang="scss" scoped>
.dashboard {
  .page-title {
    margin-bottom: 30px;

    h1 {
      font-size: 28px;
      color: #333;
      margin-bottom: 8px;
    }

    p {
      color: #666;
      font-size: 14px;
    }
  }

  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
  }

  .stat-card {
    background: white;
    border-radius: 8px;
    padding: 24px;
    display: flex;
    align-items: center;
    gap: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);

    .stat-icon {
      width: 56px;
      height: 56px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 24px;
    }

    .stat-content {
      .stat-value {
        font-size: 28px;
        font-weight: 700;
        color: #333;
        margin-bottom: 4px;
      }

      .stat-label {
        font-size: 14px;
        color: #666;
      }
    }
  }

  .quick-actions, .system-info {
    margin-bottom: 30px;

    h2 {
      font-size: 20px;
      color: #333;
      margin-bottom: 20px;
    }
  }

  .actions-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 20px;
  }

  .action-card {
    background: white;
    border-radius: 8px;
    padding: 30px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    color: #333;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    transition: all 0.3s;

    .el-icon {
      font-size: 32px;
      color: #2CB5BE;
    }

    span {
      font-size: 14px;
    }

    &:hover {
      transform: translateY(-4px);
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
    }
  }

  .info-card {
    background: white;
    border-radius: 8px;
    padding: 24px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  }

  .info-item {
    display: flex;
    justify-content: space-between;
    padding: 12px 0;
    border-bottom: 1px solid #f0f0f0;

    &:last-child {
      border-bottom: none;
    }

    .info-label {
      color: #666;
      font-size: 14px;
    }

    .info-value {
      color: #333;
      font-size: 14px;
      font-weight: 500;
    }
  }
}
</style>

