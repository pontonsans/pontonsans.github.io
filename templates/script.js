// script.js - 内容切换功能的交互逻辑

// 使用 'DOMContentLoaded' 事件确保在整个 HTML 文档被完全加载和解析完毕之后再运行脚本
document.addEventListener('DOMContentLoaded', function() {

    // 步骤1：获取所有需要的元素
    // 获取所有的按钮，它会返回一个类似数组的列表 (NodeList)
    const tabButtons = document.querySelectorAll('.tab-button');

    // 步骤2：为每个按钮添加点击事件
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            // 当任何一个按钮被点击时，执行以下操作：

            // a. 重置状态：移除所有按钮的 'active' 类
            tabButtons.forEach(btn => {
                btn.classList.remove('active');
            });

            // b. 设置新状态：给刚刚被点击的按钮添加 'active' 类
            button.classList.add('active');

            // c. 切换内容面板
            // 先隐藏所有的内容面板
            const contentPanels = document.querySelectorAll('.content-panel');
            contentPanels.forEach(panel => {
                panel.classList.remove('active');
            });

            // 再显示与被点击按钮对应的那一个面板
            // `button.dataset.tab` 会获取到按钮上的 data-tab 属性值 (如 "panel1")
            const targetPanelId = button.dataset.tab;
            const targetPanel = document.getElementById(targetPanelId);
            if (targetPanel) {
                targetPanel.classList.add('active');
            }
        });
    });
});
