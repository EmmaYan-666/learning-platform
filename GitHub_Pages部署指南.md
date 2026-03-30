# GitHub Pages 部署指南 🚀

## 📋 准备工作

### 1. 注册GitHub账号
如果还没有GitHub账号：
- 访问：https://github.com
- 点击 "Sign up" 注册
- 选择免费账户（Free）

### 2. 安装Git（如果还没有）
macOS通常已预装Git，检查一下：
```bash
git --version
```

如果没有安装，会自动提示安装。

---

## 🎯 方法一：通过GitHub网页上传（最简单）

### 步骤1：创建新仓库

1. 登录GitHub
2. 点击右上角的 "+" 号
3. 选择 "New repository"

### 步骤2：填写仓库信息

- **Repository name**: `learning-platform`（或其他名字）
- **Description**: `儿童学习游戏平台`
- **Public** ✓（必须选Public才能使用免费GitHub Pages）
- **勾选** "Add a README file"
- **点击** "Create repository"

### 步骤3：上传文件

1. 进入刚创建的仓库
2. 点击 "Add file" → "Upload files"
3. 将 `learning_platform.html` 拖拽到页面
4. 重命名为 `index.html`（重要！这样访问时就不需要加文件名）
5. 点击 "Commit changes"

### 步骤4：启用GitHub Pages

1. 在仓库页面点击 "Settings"
2. 左侧菜单找到 "Pages"
3. **Source** 选择：
   - Branch: `main`
   - Folder: `/ (root)`
4. 点击 "Save"

### 步骤5：访问你的应用

等待1-2分钟后，访问：
```
https://你的用户名.github.io/learning-platform/
```

---

## 🛠️ 方法二：使用Git命令行（推荐）

### 步骤1：创建仓库
在GitHub网页上创建仓库（同方法一的步骤1-2）

### 步骤2：初始化本地仓库

```bash
# 进入项目目录
cd /Users/emma/WorkBuddy/20260312092945

# 初始化git仓库
git init

# 创建README文件
echo "# 儿童学习游戏平台" > README.md

# 添加所有文件到暂存区
git add learning_platform.html

# 重命名为index.html
git mv learning_platform.html index.html

# 提交
git commit -m "首次提交：儿童学习游戏平台"
```

### 步骤3：连接到GitHub仓库

```bash
# 添加远程仓库（替换成你的用户名）
git remote add origin https://github.com/你的用户名/learning-platform.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

### 步骤4：启用GitHub Pages
（同方法一的步骤4）

---

## ✅ 验证部署

部署成功后，你会看到：
- Settings → Pages 页面显示绿色提示
- 显示你的网站URL

访问URL，应该能看到你的学习平台！

---

## 🎨 自定义域名（可选）

如果你有自己的域名：

1. 在仓库根目录创建 `CNAME` 文件
2. 文件内容写你的域名，例如：`learning.yourdomain.com`
3. 在域名服务商处添加CNAME记录指向 `你的用户名.github.io`

---

## 📝 更新应用

以后要更新应用：

```bash
# 修改文件后
git add index.html
git commit -m "更新功能"
git push
```

GitHub会自动重新部署，通常几秒钟就生效。

---

## 🔧 常见问题

### Q1: 为什么显示404？
- 检查文件是否命名为 `index.html`
- 确认仓库是Public
- 等待1-2分钟让部署完成

### Q2: 如何查看部署状态？
- Settings → Pages 可以看到部署状态
- 点击URL查看网站

### Q3: 语音功能不工作？
- GitHub Pages默认使用HTTPS，语音功能需要HTTPS支持
- 你的应用已经兼容HTTPS，应该可以正常工作

---

## 📱 分享给他人

部署完成后，你可以：
1. 直接发送链接给他人
2. 生成二维码分享
3. 嵌入到其他网站

**示例地址格式**：
```
https://你的用户名.github.io/learning-platform/
```

---

## 💡 提示

- 免费版GitHub Pages不支持服务端代码（PHP、Python等）
- 但你的应用是纯前端HTML，完美适配！
- 每次推送代码，GitHub自动重新部署

---

## 🚀 快速开始

**最快方式**：
1. GitHub创建仓库
2. 网页上传文件（重命名为index.html）
3. Settings启用Pages
4. 等待1-2分钟访问

**专业方式**：
使用Git命令行，方便后续更新维护

---

**祝部署顺利！** 🎉
