<template>
    <el-main>
    <el-row :gutter="12">
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <el-icon class="float-left" name="el-icon-user-solid">
                <Login />
            </el-icon>
            <span>Login</span>
          </div>
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="用户名" prop="username">
              <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input v-model="form.password" placeholder="请输入密码"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm('form')">登录</el-button>
            </el-form-item>
          </el-form>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>注册</span>
          </div>
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="用户名" prop="username">
              <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input v-model="form.password" placeholder="请输入密码"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="password">
              <el-input v-model="form.password" placeholder="请再次输入密码"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm('form')">注册</el-button>
            </el-form-item>
          </el-form>
        </el-card>
      </el-col>
    </el-row>
</el-main>
  </template>
  
<script>
    export default {
      data() {
        return {
          form: {
            username: '',
            password: ''
          }
        };
      },
      methods: {
        submitForm(formName) {
          this.$refs[formName].validate((valid) => {
            if (valid) {
              this.$message({
                type: 'success',
                message: '登录成功'
              });
            } else {
              console.log('error submit!!');
              return false;
            }
          });
        }
      }
    };
</script>