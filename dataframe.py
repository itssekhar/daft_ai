
import daft

# df = daft.from_pydict({
#     "A": [1, 2, 3, 4],
#     "B": [1.5, 2.5, 3.5, 4.5],
#     "C": [True, True, False, False],
#     "D": [None, None, None, None],
# })

#df = daft.read_csv("/Users/som/Daft_AI/archive/zillow.csv")
df = daft.read_csv("/Users/som/Daft_AI/archive/grades.csv")

   

print(df)
print(df.collect(num_preview_rows=None))

#print(df.show(4))

