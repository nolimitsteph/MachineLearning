# # #question 1
# # import pandas as pd
# #
# # mushroom = pd.read_csv(
# #     "agaricus-lepiota.data",
# #     header=None
# # )
# #
# # print(mushroom.shape)
# # print(mushroom.info())
# #
# # newcols = list(mushroom.columns)
# # newcols[0] = "edibility"
# # newcols[5] = "odor"
# # mushroom.columns = newcols
# #
# # odor_map = {
# #     "a": "almond",
# #     "l": "anise",
# #     "c": "creosote",
# #     "y": "fishy",
# #     "f": "foul",
# #     "m": "musty",
# #     "n": "none",
# #     "p": "pungent",
# #     "s": "spicy"
# # }
# #
# # mushroom["odor"] = mushroom["odor"].replace(odor_map)
# # mushroom["edibility"] = mushroom["edibility"].replace({
# #     "e": "edible",
# #     "p": "poisonous"
# # })
# #
# #
# question 2
# import pandas as pd
#
# nutri = pd.read_excel("nutrition_elderly.xls")
# consumption = {
#     0: "Never",
#     1: "Less than once a week",
#     2: "Once a week",
#     3: "2-3 times a week",
#     4: "4-6 times a week",
#     5: "Every day"
# }
#
# nutri["gender"] = nutri["gender"].replace({
#     1: "Male", 2: "Female"
# }).astype("category")
#
# nutri["situation"] = nutri["situation"].replace({
#     1: "Single",
#     2: "Living with spouse",
#     3: "Living with family",
#     4: "Living with someone else"
# }).astype("category")
#
# for col in ["meat", "fish", "raw_fruit", "cooked_fruit_veg", "chocol"]:
#     nutri[col] = nutri[col].replace(consumption).astype("category")
#
# nutri["fat"] = nutri["fat"].replace({
#     1: "Butter",
#     2: "Margarine",
#     3: "Peanut oil",
#     4: "Sunflower oil",
#     5: "Olive oil",
#     6: "Mix of vegetable oils",
#     7: "Colza oil",
#     8: "Duck or goose fat"
# }).astype("category")
#
# nutri["tea"] = nutri["tea"].astype("int64")
# nutri["coffee"] = nutri["coffee"].astype("int64")
#
# for col in ["height", "weight", "age"]:
#     nutri[col] = nutri[col].astype("float64")
#
# nutri.to_csv("nutri_modified.csv", index=False)
#
# print(nutri.dtypes)

import pandas as pd
scores = pd.DataFrame({
    "Student": [1, 2, 3, 4, 5],
    "Before": [75, 30, 100, 50, 60],
    "After": [85, 50, 100, 52, 65]
})

scores_long = scores.melt(
    id_vars="Student",
    var_name="Time",
    value_name="Score"
)

scores_long = scores_long[["Score", "Time", "Student"]]
print(scores_long)
