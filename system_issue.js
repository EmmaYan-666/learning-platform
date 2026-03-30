const pptxgen = require("pptxgenjs");

// Create presentation
let pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';
pres.author = 'WorkBuddy';
pres.title = '系统数据同步问题分析';

// Define color palette - Midnight Executive
const colors = {
  primary: '1E2761',      // Navy blue
  secondary: 'CADCFC',    // Ice blue
  accent: 'F96167',       // Coral red for problems
  white: 'FFFFFF',
  text: '2C3E50',
  lightGray: 'F8F9FA',
  success: '2C5F2D',      // Forest green for solutions
  warning: 'F39C12'       // Orange for warnings
};

let slide = pres.addSlide();

// Background
slide.background = { color: colors.white };

// Title
slide.addText("系统数据同步问题分析与解决方案", {
  x: 0.5, y: 0.3, w: 9, h: 0.6,
  fontSize: 32, fontFace: "Arial", bold: true,
  color: colors.primary, margin: 0
});

// ========== Section 1: System Architecture (Top Left) ==========
// Section title
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.0, w: 0.08, h: 0.35,
  fill: { color: colors.primary }
});
slide.addText("系统架构", {
  x: 0.7, y: 1.0, w: 2, h: 0.35,
  fontSize: 16, fontFace: "Arial", bold: true,
  color: colors.primary, margin: 0
});

// B360 box
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 0.5, y: 1.5, w: 1.6, h: 0.8,
  fill: { color: colors.primary }, rectRadius: 0.05
});
slide.addText("B360\n中央预定系统", {
  x: 0.5, y: 1.5, w: 1.6, h: 0.8,
  fontSize: 11, fontFace: "Arial", bold: true,
  color: colors.white, align: "center", valign: "middle", margin: 0
});

// OXI interface box
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 2.5, y: 1.5, w: 1.2, h: 0.8,
  fill: { color: colors.secondary }, rectRadius: 0.05
});
slide.addText("OXI\n接口", {
  x: 2.5, y: 1.5, w: 1.2, h: 0.8,
  fontSize: 11, fontFace: "Arial", bold: true,
  color: colors.primary, align: "center", valign: "middle", margin: 0
});

// PMS box
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 4.1, y: 1.5, w: 1.6, h: 0.8,
  fill: { color: colors.primary }, rectRadius: 0.05
});
slide.addText("PMS\n酒店管理系统", {
  x: 4.1, y: 1.5, w: 1.6, h: 0.8,
  fontSize: 11, fontFace: "Arial", bold: true,
  color: colors.white, align: "center", valign: "middle", margin: 0
});

// Arrows between boxes
slide.addShape(pres.shapes.RIGHT_ARROW, {
  x: 2.15, y: 1.75, w: 0.3, h: 0.3,
  fill: { color: colors.text }
});
slide.addShape(pres.shapes.RIGHT_ARROW, {
  x: 3.75, y: 1.75, w: 0.3, h: 0.3,
  fill: { color: colors.text }
});

// Sync mechanism note
slide.addText([
  { text: "同步机制: ", options: { bold: true } },
  { text: "异步消息队列 + 全量覆盖" }
], {
  x: 0.5, y: 2.45, w: 5.2, h: 0.3,
  fontSize: 10, fontFace: "Arial",
  color: colors.text, margin: 0
});

// ========== Section 2: Problem Description (Top Right) ==========
// Section title
slide.addShape(pres.shapes.RECTANGLE, {
  x: 5.9, y: 1.0, w: 0.08, h: 0.35,
  fill: { color: colors.accent }
});
slide.addText("业务场景与问题", {
  x: 6.1, y: 1.0, w: 3, h: 0.35,
  fontSize: 16, fontFace: "Arial", bold: true,
  color: colors.accent, margin: 0
});

// Problem content
slide.addText([
  { text: "业务需求:", options: { bold: true, breakLine: true } },
  { text: "会员SLC权益满足条件时，自动添加special code到订单", options: { breakLine: true } },
  { text: "\n核心问题:", options: { bold: true, breakLine: true } },
  { text: "• B360处理SLC逻辑，订单双向同步", options: { breakLine: true } },
  { text: "• PMS FO修改订单时，B360推送更新可能失败", options: { breakLine: true } },
  { text: "• 全量覆盖导致PMS新修改内容丢失（如Comments）", options: { breakLine: true } }
], {
  x: 5.9, y: 1.4, w: 3.6, h: 1.6,
  fontSize: 10, fontFace: "Arial",
  color: colors.text, margin: 0, valign: "top"
});

// ========== Section 3: Problem Flow (Middle) ==========
// Section title
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 2.95, w: 0.08, h: 0.35,
  fill: { color: colors.accent }
});
slide.addText("问题流程示意", {
  x: 0.7, y: 2.95, w: 2.5, h: 0.35,
  fontSize: 16, fontFace: "Arial", bold: true,
  color: colors.accent, margin: 0
});

// Step 1: PMS FO modifies order
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 0.5, y: 3.5, w: 2.0, h: 0.6,
  fill: { color: colors.lightGray }, rectRadius: 0.05,
  line: { color: colors.text, width: 1 }
});
slide.addText("① PMS FO修改订单\n(添加Comments)", {
  x: 0.5, y: 3.5, w: 2.0, h: 0.6,
  fontSize: 10, fontFace: "Arial",
  color: colors.text, align: "center", valign: "middle", margin: 0
});

// Arrow
slide.addShape(pres.shapes.RIGHT_ARROW, {
  x: 2.55, y: 3.65, w: 0.4, h: 0.3,
  fill: { color: colors.warning }
});

// Step 2: Sync to B360
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 3.0, y: 3.5, w: 2.0, h: 0.6,
  fill: { color: colors.lightGray }, rectRadius: 0.05,
  line: { color: colors.text, width: 1 }
});
slide.addText("② 同步至B360\n触发SLC逻辑", {
  x: 3.0, y: 3.5, w: 2.0, h: 0.6,
  fontSize: 10, fontFace: "Arial",
  color: colors.text, align: "center", valign: "middle", margin: 0
});

// Arrow
slide.addShape(pres.shapes.RIGHT_ARROW, {
  x: 5.05, y: 3.65, w: 0.4, h: 0.3,
  fill: { color: colors.accent }
});

// Step 3: B360 pushes back
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 5.5, y: 3.5, w: 2.2, h: 0.6,
  fill: { color: 'FEE2E2' }, rectRadius: 0.05,
  line: { color: colors.accent, width: 2 }
});
slide.addText("③ B360推回更新\n(删除special code)", {
  x: 5.5, y: 3.5, w: 2.2, h: 0.6,
  fontSize: 10, fontFace: "Arial", bold: true,
  color: colors.accent, align: "center", valign: "middle", margin: 0
});

// Arrow
slide.addShape(pres.shapes.RIGHT_ARROW, {
  x: 7.75, y: 3.65, w: 0.4, h: 0.3,
  fill: { color: colors.accent }
});

// Step 4: Problem
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 8.2, y: 3.3, w: 1.3, h: 1.0,
  fill: { color: colors.accent }, rectRadius: 0.05
});
slide.addText("❌ 更新失败\n或\n覆盖新数据", {
  x: 8.2, y: 3.3, w: 1.3, h: 1.0,
  fontSize: 10, fontFace: "Arial", bold: true,
  color: colors.white, align: "center", valign: "middle", margin: 0
});

// ========== Section 4: Solution (Bottom) ==========
// Section title
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 4.55, w: 0.08, h: 0.35,
  fill: { color: colors.success }
});
slide.addText("建议解决方案", {
  x: 0.7, y: 4.55, w: 2.5, h: 0.35,
  fontSize: 16, fontFace: "Arial", bold: true,
  color: colors.success, margin: 0
});

// Solution box
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 5.0, w: 9.0, h: 0.5,
  fill: { color: 'E8F5E9' },
  line: { color: colors.success, width: 1 }
});

slide.addText([
  { text: "将SLC权益逻辑迁移至PMS端处理 → ", options: { bold: true } },
  { text: "PMS本地监控订单变更，自动决定special code更新 → 所有变更由PMS统一发起 → B360仅作为数据接收方 → 避免双向覆盖冲突" }
], {
  x: 0.6, y: 5.0, w: 8.8, h: 0.5,
  fontSize: 11, fontFace: "Arial",
  color: colors.text, margin: 0, valign: "middle"
});

// Save
pres.writeFile({ fileName: "/Users/emma/WorkBuddy/20260312092945/系统数据同步问题.pptx" });
