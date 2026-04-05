import matplotlib.pyplot as plt

def visualize_results(train, test, pred):
    plt.figure(figsize=(10,5))
    plt.plot(train, label='Train')
    plt.plot(test,label='Test')
    plt.plot(pred,label='Pred')
    plt.legend()
    plt.show()