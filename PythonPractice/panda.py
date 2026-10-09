import pandas as pd

data = {
    "institution_name": [
        "Auckland",
        "Waikato",
        "Canterbury",
        "Auckland"
    ]
}

dataframe = pd.DataFrame(data)

encoded_data = pd.get_dummies(
    dataframe,
    columns=["institution_name"],
    dtype=int
)

print(encoded_data)