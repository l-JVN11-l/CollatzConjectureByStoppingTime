import matplotlib.pyplot as plt


def byNumber(sum, count, startingList: list):
  outputNum = int(sum)

  if outputNum % 2 == 0:
    outputNum /= 2
  else:
    outputNum *= 3
    outputNum += 1

  if outputNum == 1:
    stoppingTime2.append(int(outputNum))
  else:
    byNumber(outputNum, count + 1, startingList)
    stoppingTime2.append(int(outputNum))


if __name__ == "__main__":
  num = int(input("What number?: "))
  stoppingTime2 = []
  stoppingTime = []
  length = 0

  for _ in range(0, num):
    byNumber(abs(_ - num), 0, [])
    length = len(stoppingTime2) + 1

    stoppingTime2.clear()
    stoppingTime.append(length)

  print(stoppingTime)

  plt.plot(list(reversed(stoppingTime)), 'b.')
  plt.xlabel("Number")
  plt.ylabel("Stopping Time Value")
  plt.show()
