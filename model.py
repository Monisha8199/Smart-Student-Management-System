import torch
import torch.nn as nn

class MiniGPT(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(MiniGPT, self).__init__()

        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.fc = nn.Linear(embedding_dim, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        x = x.mean(dim=1)
        x = self.fc(x)
        return x


# Run this file directly
if __name__ == "__main__":

    vocab_size = 100
    embedding_dim = 32

    model = MiniGPT(vocab_size, embedding_dim)

    # Dummy input (batch_size=2, sequence_length=5)
    sample_input = torch.randint(0, vocab_size, (2, 5))

    output = model(sample_input)

    print("Input:")
    print(sample_input)

    print("\nOutput Shape:")
    print(output.shape)

    print("\nOutput:")
    print(output)