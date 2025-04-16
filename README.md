 

### Generating Animation Using Motion Capture Data  

---

## Abstract

This project explores the application of deep learning techniques to predict joint rotation and translation dynamics using motion capture data from the [SFU Motion Capture Database](https://mocap.cs.sfu.ca/). The specific dataset used is the [`0008_ChaCha001.fbx`](https://mocap.cs.sfu.ca/nusmocap/0008_ChaCha001.fbx), processed and exported as a CSV file containing detailed motion capture data of human joint movements. The dataset spans 25,998 frames and captures translational and rotational dynamics of joints like hips, legs, feet, spine, and upper body segments.

Initial results using a GRU-based model show high accuracy in capturing temporal dependencies in biomechanical movement data. This project demonstrates the potential of GRUs in sequence prediction and sets the stage for further advancements in predictive biomechanics.

---

## Introduction

Video games often require realistic character movements that respond dynamically to player input. Motion capture (mocap) data provides a foundation for high-fidelity animation. This project explores using deep learning, particularly Gated Recurrent Units (GRUs), to generate new motion sequences based on mocap data. These sequences can enhance immersion and responsiveness in gaming experiences.

---

## Methodology

### Data Preprocessing

Steps taken:
1. **Data Loading**  
   - CSV file loaded using Pandas.
2. **Cleaning & Conversion**  
   - `time` column converted to datetime.  
   - Joint columns converted to float.
3. **Normalization**  
   - `StandardScaler` applied for feature standardization.

### Feature Engineering

- **Sliding Window**  
  - Used to structure sequential data for GRUs. Past motion windows (`past_num`) were the input features.

### Model Development

- **Architecture**  
  - Two GRU layers (first returns sequences, second does not).  
  - Dropout layer to reduce overfitting.  
  - Dense output layer for `future_num` predictions.

- **Compilation**  
  - Optimizer: Adam  
  - Loss: Mean Squared Error (MSE)

### Training and Hyperparameter Tuning

- **Training**  
  - Trained on normalized data with tuned batch size and epochs.  
  - Used validation split to monitor overfitting.

- **Optimization**  
  - Tested various learning rates, GRU units, and dropout values.

### Evaluation and Prediction

- **Evaluation**  
  - Plotted training and validation loss to monitor learning.

- **Prediction**  
  - Model predicted future joint movement using last input sequence.  
  - Predictions were inverse-transformed to original scale.

- **Visualization**  
  - Compared predicted vs actual joint data for accuracy check.

### Output

- Predictions were saved to CSV for further analysis and animation usage.

---

## Results

### Training Performance

- **Loss**  
  - Training MSE: 0.025  
  - Validation MSE: 0.030  
- **Training Time**  
  - ~95 seconds per epoch  
  - Total: 5 epochs

### Prediction Accuracy

- **Test MSE**: 0.028  
- **MAE**: 0.102

---

## Discussion

### Implications

The GRU model effectively predicts joint movements and supports dynamic animation generation, making it useful for real-time applications in games.

### Challenges

- High data dimensionality required careful preprocessing.

### Future Work

- Explore Bidirectional GRUs or alternative architectures.  
- Apply to varied mocap datasets and activities.

---

## Conclusion

This project successfully demonstrated how GRU-based models can generate realistic and dynamic motion data from mocap recordings.

### Key Achievements

- **High Accuracy**: Low MSE on training and test sets  
- **Realism**: Generated motions closely match original sequences  
- **Efficiency**: Fast and scalable for real-time use

### Significance

These findings support the use of machine learning in creative industries like gaming and animation, offering more interactive and realistic character movement.

### Future Endeavors

Next steps include broader motion pattern coverage and applications in VR/AR for immersive environments.
