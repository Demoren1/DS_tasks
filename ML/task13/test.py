import model_ssd300
import torch

# Создаём модель
model_aux = model_ssd300.AuxiliaryConvolutions()

# Входной тензор
x = torch.randn(1, 1024, 19, 19)  # batch_size=1, channels=1024, height=19, width=19

# Проверяем размеры на каждом этапе
model_aux.forward_test(x)
