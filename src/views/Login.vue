<template>
  <div class="login-page">
    <el-card class="login-card" shadow="hover">
      <h1 class="title">访问验证</h1>
      <p class="subtitle">请输入访问密码</p>
      <el-form @submit.prevent="handleLogin">
        <el-form-item>
          <el-input
            v-model="password"
            placeholder="请输入密码"
            show-password
            size="large"
            @keyup.enter="handleLogin"
          />
        </el-form-item>
        <el-button type="primary" size="large" class="login-btn" @click="handleLogin">
          登录
        </el-button>
      </el-form>
    </el-card>
  </div>
</template>

<script>
const AUTH_KEY = 'local_v_logged_in'
const PASSWORD = import.meta.env.VITE_LOGIN_PASSWORD || '123456'

export default {
  name: 'LoginPage',
  data() {
    return {
      password: ''
    }
  },
  methods: {
    handleLogin() {
      if (this.password !== PASSWORD) {
        this.$message.error('密码错误')
        return
      }

      sessionStorage.setItem(AUTH_KEY, '1')
      const redirectPath = this.$route.query.redirect || '/'
      this.$router.replace(redirectPath)
    }
  }
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #e8f0ff 0%, #f8fbff 100%);
  padding: 20px;
}

.login-card {
  width: 100%;
  max-width: 420px;
  border-radius: 12px;
}

.title {
  margin: 0 0 8px;
  text-align: center;
  color: #1f2937;
}

.subtitle {
  margin: 0 0 20px;
  text-align: center;
  color: #6b7280;
}

.login-btn {
  width: 100%;
}
</style>
