from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.model import train_model
from src.evaluate import evaluate_model
from src.visualize import visualize_results
from src.llm_parser import parse_user_input

df=load_data('data/AMAZON_daily.csv')
df=preprocess_data(df)
train_size=int(len(df)*0.8)
train, test= df[:train_size],df[train_size:]
model = train_model(train)
user_query = input("Enter your request:")
parsed_query = parse_user_input(user_query)
horizon = parsed_query['horizon']
fh = list(range(1, horizon + 1))
pred=model.predict(fh=fh)
test_subset = test[:horizon] 
mae = evaluate_model(test_subset, pred)
print(f"MAE: {mae}")
visualize_results(train, test, pred)