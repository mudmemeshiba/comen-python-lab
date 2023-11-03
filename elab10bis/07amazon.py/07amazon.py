import json

def read_file(filename):
    with open(filename) as f:
        dataLst = []
        data = f.readlines()
        for i in data:
            data = json.loads(i)
            dataLst.append(data)
    return dataLst

def amazon(data, inp):
    if inp == 1:
        print(len(data))

    if inp == 2:
        reviewerID = []
        user = 0
        for i in data:
            if i['reviewerID'] not in reviewerID:
                reviewerID.append(i['reviewerID'])
                user += 1
        print(user)
    
    if inp == 3:
        productName = []
        product = 0
        for i in data:
            if i['productName'] not in productName:
                productName.append(i['productName'])
                product += 1
        print(product)

    if inp == 4:
        catLst = []
        count = 0
        for i in data:
            if i['category'] != None:
                cat = i['category'].split('>')
                if cat[0].strip() not in catLst:
                    catLst.append(cat[0].strip())
                    count += 1
        print(count)

    if inp == 5:
        catLst = []
        count = 0
        for i in data:
            if i['category'] != None:
                cat = i['category'].split('>')
                if cat[1].strip() not in catLst:
                    catLst.append(cat[1].strip())
                    count += 1
        print(count)

    if inp == 6:
        reviewCount = {} 
        for i in data:
            if i['reviewerID'] != None:
                if i['reviewerID'] not in reviewCount:
                    reviewCount.update({i['reviewerID']:1})
                else:
                    reviewCount[i['reviewerID']] += 1
        sortedReview = sorted(reviewCount.items(), key = lambda x: x[1], reverse=True)
        print(sortedReview[0][0])

    if inp == 7:
        avgRating = {}
        for i in data:
            if i['productName'] not in avgRating:
                avgRating.update({i['productName']:[]})
            avgRating[i['productName']].append(i['overall'])

        avgRatingList = []
        for j in avgRating:
            avgRatingList.append([j, sum(avgRating[j])/len(avgRating[j]), len(avgRating[j])])
        sortedAvgRatingList = sorted(avgRatingList, key=lambda x: x[2], reverse=True)
        # print(sortedAvgRatingList)
        sortedReviewCount = sorted(sortedAvgRatingList, key=lambda x: x[1], reverse=True)
        # print(sortedReviewCount)
        print(sortedReviewCount[0][0])

        # sameRating = {}
        # for k in range(len(sortedAvgRating)-1):
        #     sameRating.update({sortedAvgRating[k][0]: sortedAvgRating[k][1]})
        #     if sortedAvgRating[k][1] == sortedAvgRating[k+1][1]:
        #         sameRating.update({sortedAvgRating[k+1][0]: sortedAvgRating[k+1][1]})
            
        # reviewCount = {} 
        # for p in data:
        #     if p['productName'] != None:
        #         if p['productName'] not in reviewCount:
        #             reviewCount.update({p['productName']:1})
        #         else:
        #             reviewCount[p['productName']] += 1
        # sortedReviewCount = dict(sorted(reviewCount.items(), key = lambda x: x[1], reverse=True))

        # for i in sortedReviewCount:
        #     if i == 'Tripp Lite Isobar 4 Outlet Surge Protector Power Strip, 6ft Cord, Right-Angle Plug, Metal, Lifetime Limited Warranty & $50,000 INSURANCE (ISOBAR4ULTRA)':
        #         print(sortedReviewCount[i])
        
    if inp == 8:
        product = {}
        for i in data:
            if i['productName'] not in product:
                product.update({i['productName']:[]})       
            words = []
            words.append(i['reviewText'].split(' '))
            countWord = len(words[0])
            product[i['productName']].append(countWord)
        for j in product:
            product.update({j:sum(product[j])/len(product[j])})
        sortedAvg = sorted(product.items(), key=lambda x: x[1], reverse=True)
        print(sortedAvg[0][0])
   
fn = input("file name: ")

# x = 1
# y = "2"
# x + y
inp = int(input("input: "))
data = read_file(fn)
amazon(data, inp)

# for word in words[0]:
#     if word.isalpha() == False:
#         words[0].remove(word)
# print(' '.join(words[0]))