# pairwise-astro-stack-drift

## 领域

游戏、图形与多媒体

## 主题

星野长曝光堆栈对齐

## 说明

分区畸变校正、首帧基准与锐度加权。

初始状态下 `imaging/astro_stack_drift.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
