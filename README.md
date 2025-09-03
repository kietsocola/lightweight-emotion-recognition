# 🎭 Facial Emotion Recognition under Low-Light Conditions  

Lightweight **CNN-based emotion recognition system** using **MobileNetV3-Small** and **adaptive data augmentation** on the **FER2013 dataset**.  

---

## 🚀 Highlights  
- **Model**: MobileNetV3-Small (optimized for low-resource devices).  
- **Adaptive augmentation**: Gamma correction, CLAHE, contrast stretching (auto-selected based on image brightness).  
- **Dataset**: FER2013 (7 emotions: 😀 😢 😠 😲 😐 😨 🤢).  

---

## 📊 Results  

| Model               | Dataset                  | Accuracy (%) | Size (MB) | Inference (ms/img) |
|---------------------|--------------------------|--------------|-----------|---------------------|
| MobileNetV3-Small   | FER2013 (original)       | 61.63        | 13.5      | 2.12                |
| MobileNetV3-Small   | FER2013 (low-light + aug)| 61.55 (+2.7%)| 13.5      | 2.12                |
| ResNet18            | FER2013 (low-light + aug)| 67.48        | 42.7      | 2.91                |

✅ **Key finding**: Adaptive augmentation improves robustness under low-light while keeping the model lightweight.  

---

## 🔧 Tech Stack  
- **Frameworks**: Python, PyTorch  
- **Training**: Google Colab  
- **Evaluation**: MacBook Air M1  
- **EDA**: PCA, histogram analysis  

---

## 🌟 Practical Impact  
- Reliable **facial emotion recognition** under poor lighting.  
- Suitable for **edge devices, IoT, surveillance cameras, and mobile apps**.  

---

👨‍💻 Developed as part of **Scientific Research Methodology (PPNCKH) course project** – University of Saigon.  
