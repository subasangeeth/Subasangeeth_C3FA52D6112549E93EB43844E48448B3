def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:  # Use '==' to check for equality
      indices.append(index)

  return indices


products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'

result = linearSearchProduct(products, target)
print(result)
