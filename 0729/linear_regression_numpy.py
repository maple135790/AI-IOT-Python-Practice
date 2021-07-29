import numpy as np

data_points = np.array([[0.11, 1.24],  
                        [0.20, 1.40], 
                        [0.49, 2.00],
                        [0.65, 2.27],
                        [0.67, 2.41],
                        [0.83, 2.52]])

a =np.random.randn(1)
b =np.random.randn(1)
print(a,b)

"""Step 2: repeatedly visit entire dataset for N epochs"""

n_epoch =1000
batch_size =2
eta =0.01  # learning rate

for epoch in range(n_epoch):
  # Step 2.1: shuffle the data point
  np.random.shuffle(data_points)

  # Step 2.2:
  for i in range(0,len(data_points),batch_size):
    points =data_points[i:i+batch_size]
    
    x =points[:,0]
    y =points[:,1]

    # compute MSE loss
    y_pred = a *x +b
    y_err =y - y_pred
    mse_loss = (y_err**2).mean()

    # compute the gradients w.r.t a and b
    a_grad =-2.0*((y_err *x).mean())
    b_grad =-2.0*(y_err.mean())

    # update a and b (model parameter)
    a =a -eta *a_grad
    b =b -eta *b_grad

    print('grad:{} {} {}'.format(a,b,mse_loss))