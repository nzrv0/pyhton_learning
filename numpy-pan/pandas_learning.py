import pandas as pd
import numpy as np

# a one-dimensional labeled array holding data of any type such as integers, strings, Python objects etc.
series = pd.Series([1, np.nan, 3, 4, "ss"])

dates = pd.date_range("20130101", periods=6)

# a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns.
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

# print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
# print(df2.dtypes) # data has diffrenet types

df2.head()  # deafult gives 4 element row but we can specifiy
df2.tail()

# getting columns and indexes
df2.index
df2.columns

# converting to nupy array
df.to_numpy()
df2.to_numpy()  # pandas will get common data type which in this case is object


# shows a quick statistic summary of your data
df.describe()

# transposing data
df.T


### Sorting
# sort_index with axis=0 sorts the index, and this ordering is then used to set the order of the rows.
# sort_index with axis=1 sorts the column headers, and this ordering is then used to set the order of the columns.

df.sort_index(axis=0, ascending=False)  # this same with df.sort_index(ascending=False)

# sorting by the values
df.sort_values(by="B")


### Selecting
df["A"]  # selecting by column
df[:4]  # by rows
df["20130102":"20130104"]  # same

# for all columns return this rows
df.loc[dates[0]]
df.loc[:, ["A", "B"]]  # return every rows for these columns
df.loc["20130102":"20130104", ["A", "B"]]
df.loc[dates[0], "A"]

# for accesing single value
df.at[dates[0], "A"]  # fast

# selecting by position
dd = df.iloc[2]
df.iloc[3:5, 0:2]  # rows and cols
df.iloc[[1, 2, 4], [0, 2]]  # by position
df.iat[1, 1]  # fast for single element

# boolean indexing
df[df["A"] > 0]
df[df > 0]

# isin()
df3 = df.copy()
df3["E"] = ["one", "one", "two", "three", "four", "three"]
df3[df3["E"].isin(["two", "four"])]

# setting
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
df["F"] = s1

df.at[dates[0], "A"] = 0
df.iat[0, 1] = 0  # setting value by position
df.loc[:, "D"] = np.array([5] * len(df))


### Missing data
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1

# drops any row that has value non
df1.dropna(how="any")

# fills any row that has value non
df1.fillna(value=5)

# gets any row that has value non
pd.isna(df1)


### Stats
df.mean()  # finding mean value. also we can find mean value by rows with axis=1
df.sub(s1, axis="index")  # substracts element rows with this values

# user defined functions
dd = df.agg(lambda x: np.mean(x) * 5.6)  # calculates by column
dt = df.transform(lambda x: x * 101.2)  # calculates by row

df.value_counts()  # counts uniqe values

# string methods
df3["E"].str.capitalize()


### Merge
pieces = [df[:3], df[3:5], df[5:]]
pp = pd.concat(pieces)
# print(pp)

# enables SQL style join types
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
ds = pd.merge(left, right, on="key")
# print(ds)


### Grouping
df123 = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
dss = df123.groupby("A")[
    ["C", "D"]
].sum()  # get sum of columsn c and d for grouping by A
# print(dss)

dsss = df123.groupby(["A", "B"]).sum()


### Reshaping
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])
df403 = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
# print(df403)
stacked = df403.stack(
    future_stack=True
)  # method “compresses” a level in the DataFrame’s columns
# print(stacked)

stacked.unstack()


# pivot table
df = pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])


# Categoricals
df101 = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)
df101["grade"] = df101["raw_grade"].astype("category")
print(df101["grade"])

