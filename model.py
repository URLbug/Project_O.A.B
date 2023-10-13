from src.train import train, model


history = train()

model.save('./model/beta_resnet.h5')