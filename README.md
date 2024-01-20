This project helps a company in Artificial Intelligence and Computer Vision domain to give mobile document digitization experience by scanning documents in bulk.
- Created a model which predicts whether the page of the book is being flipped using a single image.
- Build a Convolution Neural Network (CNN) for prediction by using the PyTorch module.
- Outperformed the baseline model’s performance by achieving 98% F1 score.
- Gradually reduced the model size, up to a 5 time smaller model - maintaining the F1 score above 90%

In the second part of the project, instead of classifying a single frame, a whole sequence is classified 
- The benchmark is the single-frame model, modified to generate the sequence output using average or max pooling
- Used a Recurrent Neural Network to create the sequence memory. Improved the performance by adding skip connections - 88.8% F1 score
- To reduce training time, applied transfer learning to the CNN section of the model - 96.9% F1 score

Curious for more? Check out the Notebook in the repo
