import random
from django.shortcuts import render,get_list_or_404
from items.models import Product, Review, Category, Brand
from account.models import CustomUser
from cart_shop.models import Cart
# Create your views here.
from django.http import HttpResponse
import re
from view_product.models import UserInfo, ClickCount
import warnings
from scipy.sparse.linalg import svds
from scipy.sparse import csr_matrix
import scipy.sparse
# from sklearn.externals
import joblib
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt
import time
import json
import math
from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Avg, Max, Min, Count
# lib rec
from itertools import groupby
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from IPython.core.interactiveshell import InteractiveShell
from surprise import KNNWithMeans
from surprise import Dataset
from surprise import accuracy
from surprise import Reader
import os
from sklearn.decomposition import TruncatedSVD
from surprise.model_selection import train_test_split
InteractiveShell.ast_node_interactivity = "all"
warnings.simplefilter('ignore')



from django.shortcuts import get_object_or_404
from view_product.models import UserAction
from django.core.validators import slug_re
import re
from view_product.models import ClickCount
def main(request):
    if request.user.is_authenticated:
        recently_activate = UserAction.objects.filter(user=request.user).order_by("-timestamp")
        recently_product_real = []
        list_set = []
        for i in recently_activate:
            url = i.action
            pattern = r'/product/(.+)/$'
            match = re.search(pattern, url)
            if match:
                product_name = match.group(1)
                if product_name not in list_set:
                    list_set.append(product_name)
                    recently_product_real.append(Product.objects.get(slug=product_name))
    else:
        recently_product_real = []
    number = 0
    if request.user:
        number = Cart.objects.all().filter(user=request.user.id).count()
    categories = Category.objects.filter(image__isnull=False)
    brand = Brand.objects.filter(image__isnull=False).exclude(image__exact='')



    ratings_stats = Review.objects.values('product_id').annotate(
        mean_rating=Avg('rate'),
        rating_count=Count('rate')
    )

    # Display the ratings statistics
    product =[]
        # Assuming your model has fields like 'productId' and 'Rating'
    reviews_stats = Review.objects.values(
        'product_id').annotate(total_ratings=Count('rate'))
    filtered_products = [stats['product_id']
                         for stats in reviews_stats if stats['total_ratings'] >= 1]
    filtered_reviews = Review.objects.filter(product_id__in=filtered_products)
    mean_ratings = filtered_reviews.values(
        'product_id').annotate(mean_rating=Avg('rate'))
    sorted_ratings = sorted(
        mean_ratings, key=lambda x: x['mean_rating'], reverse=True)
    for rating_stats in sorted_ratings[:10]:  # Displaying the top 5
        product.append(Product.objects.get(id=rating_stats['product_id']))











    reviews_queryset = Review.objects.values('user_id', 'product_id', 'rate')
    reviews_df = pd.DataFrame.from_records(reviews_queryset)



# --------------------------------------------
# part3
    new_df1 = reviews_df.head(100000000)
    ratings_matrix = new_df1.pivot_table(
        values='rate', index='user_id', columns='product_id', fill_value=0)
    # print(ratings_matrix.head())
    # print(ratings_matrix.shape)
    X = ratings_matrix.T
    # print(X.head())
    X1 = X
    # Decomposing the Matrix

    SVD = TruncatedSVD(n_components=4)
    decomposed_matrix = SVD.fit_transform(X)
    # print(decomposed_matrix.shape)
    # Correlation Matrix
    correlation_matrix = np.corrcoef(decomposed_matrix)

    recently_activate = UserInfo.objects.all()
    recently_product = []
    list_set = []
    for i in recently_activate:
        url = i.referrer
        pattern = r'/product/(.+)/$'
        match = re.search(pattern, url)
        if match:
            product_name = match.group(1)
            if product_name not in list_set:
                list_set.append(product_name)
                recently_product.append(Product.objects.get(slug=product_name))
    
    recommend_product = []
    number_recommend = []
    if request.user.is_authenticated:
        user_rate = Review.objects.filter(user_id=request.user)
        for count in user_rate:
            correlation_product_ID = correlation_matrix[count.product.count]
            Recommend = list(X.index[correlation_product_ID > 0.65])
            for j in Recommend[0:10]:
                number_recommend.append(j)
        for i in set(number_recommend):
            recommend_product.append(Product.objects.get(id=i))
    for count in recently_product:
        correlation_product_ID = correlation_matrix[count.count]
        Recommend = list(X.index[correlation_product_ID > 0.65])
        for j in Recommend[0:10]:
            number_recommend.append(j)
    for i in set(number_recommend):
        recommend_product.append(Product.objects.get(id=i))
    
    query = ClickCount.objects.all().order_by('-count')
    trending = []
    for i in query:
        trending.append(i.product)

    context={
    "trending": trending[0:10],
    "recommend": recommend_product[0:10],
    "recommend2": recommend_product[10:20],
    'recently_product': recently_product_real[0:10],
    "number_product": number,
    "categories":categories,
    'brand': brand,
    'product': product[0:10],
    }
    return render(request, 'home/main.html', context)

def not_found(request, exception):

    return render(request, 'home/notfound.html',{}, status=404)


from items.models import Review
from cart_shop.models import OrderItems, Order

def test(request):
    
    review = Review.objects.all()

# Display the data
    first_review = Review.objects.first()
    # for first_review in review:
    #     if first_review:
    #         print("Review ID:", first_review.id)
    #         print("Rating:", first_review.rate)
    #         print("Product_id:", first_review.product_id)
    #         print("Comment:", first_review.comment)
    #         print("\n")
    #         # Add more attributes as needed
    #     else:
    #         print("No reviews available")

# Get the number of records (rows)
    review_count = Review.objects.all().count()
    print("Number of records:", review_count)

# Get the number of fields (columns)
    num_fields = len(Review._meta.fields)
    print("Number of fields in Review model:", num_fields)


# Check the datatypes
    review_instance = Review.objects.first()

    # if review_instance:
    #     for field_name, value in review_instance.__dict__.items():
    #         print(f"Field: {field_name}, Type: {type(value)}")
    # else:
    #     print("No records available")

# Four point summary
    # Display Average, Max, Min, Total
    reviews_stats = Review.objects.aggregate(
        average_rating=Avg('rate'),
        max_rating=Max('rate'),
        min_rating=Min('rate'),
        total_reviews=Count('rate')
    )

    # Now you can access the statistics
    average_rating = reviews_stats['average_rating']
    max_rating = reviews_stats['max_rating']
    min_rating = reviews_stats['min_rating']
    total_reviews = reviews_stats['total_reviews']
    # Display Average, Max, Min, Total
    print(
        f"Average Rating: {average_rating}, Max Rating: {max_rating}, Min Rating: {min_rating}, Total Reviews: {total_reviews}")

# Find the minimum and maximum ratings
    print('Minimum rating is: %d' % (max_rating))
    print('Maximum rating is: %d' % (min_rating))

# Check for missing values
    fields = Review._meta.fields

    # Create a dictionary to store the count of missing values for each field
    missing_values_count = {}

    # Iterate over each field and count the number of missing values
    # for field in fields:
    #     field_name = field.name
    #     missing_values_count[field_name] = Review.objects.filter(
    #         **{f"{field_name}__isnull": True}).count()

    # Print the results
    # for field_name, count in missing_values_count.items():
    #     print(f"Number of missing values for {field_name}: {count}")

    # Dropping the ID, Comment, Crated_at columns
    review = Review.objects.exclude(id__isnull=True).values().exclude(id=None)
    review = Review.objects.exclude(
        crated_at__isnull=True).values().exclude(crated_at=None)
    review = Review.objects.exclude(
        comment__isnull=True).values().exclude(comment=None)

    # Analysis of rating given by the user

    no_of_rated_products_per_user = (
        Review.objects
        .values('user')  # Group by the 'user' field
        .annotate(no_of_rated_products=Count('product', distinct=True))
    )

    # Print the results
    # for entry in no_of_rated_products_per_user:
    #     user_id = entry['user']
    #     count = entry['no_of_rated_products']
    #     print(f"User {user_id} has rated {count} products.")

    count_values = [entry['no_of_rated_products']
                    for entry in no_of_rated_products_per_user]
    total_count = sum(count_values)
    average_count = sum(count_values) / len(count_values)
    max_count = max(count_values)
    min_count = min(count_values)

    # # Print the results
    # print(f"Total Count: {total_count}")
    # print(f"Average Count: {average_count}")
    # print(f"Max Count: {max_count}")
    # print(f"Min Count: {min_count}")
    filtered_results = [
        entry for entry in no_of_rated_products_per_user if entry['no_of_rated_products'] >= 1]

# Print the filtered results
    # for entry in filtered_results:
    #     print(
    #         f"User {entry['user']} has rated {entry['no_of_rated_products']} products.")

    # Assuming your model has fields like 'productId' and 'Rating'
    # reviews_stats = Review.objects.values(
    #     'product_id').annotate(total_ratings=Count('rate'))

    # Filter products with 50 or more ratings
    # filtered_products = [stats['product_id']
    #                      for stats in reviews_stats if stats['total_ratings'] >= 1]

    # Fetch reviews for the filtered products
    # filtered_reviews = Review.objects.filter(product_id__in=filtered_products)

    # Now, filtered_reviews contains the reviews for products with 50 or more ratings
    # mean_ratings = filtered_reviews.values(
    #     'product_id').annotate(mean_rating=Avg('rate'))
    # for rating_stats in mean_ratings:
    #     print(
    #         f"Product ID: {rating_stats['product_id']}   \t   Rating: {rating_stats['mean_rating']}")

    # Sort the results by mean rating in descending order
    # sorted_ratings = sorted(
    #     mean_ratings, key=lambda x: x['mean_rating'], reverse=True)

    # Display the sorted mean ratings
    # for rating_stats in sorted_ratings[:5]:  # Displaying the top 5
    #     print(
    #         f"Product ID: {rating_stats['product_id']}, Mean Rating: {rating_stats['mean_rating']}")

    # ratings_stats = Review.objects.values('product_id').annotate(
    #     mean_rating=Avg('rate'),
    #     rating_count=Count('rate')
    # )

# Display the ratings statistics
    # for stats in ratings_stats:
    #     print(
    #         f"Product ID: {stats['product_id']}, Mean Rating: {stats['mean_rating']}, Rating Count: {stats['rating_count']}")

    # ratings_stats['rating_counts'] = pd.DataFrame(
    #     mean_ratings.groupby('productId')['Rating'].count())
# -----------------------------------------------------------
# part 2
    # Splitting the dataset
    reviews_queryset = Review.objects.values('user_id', 'product_id', 'rate')
    reviews_df = pd.DataFrame.from_records(reviews_queryset)

    # Assuming 'rate' is a numeric field (you might need to adjust the range)
    # reader = Reader(rating_scale=(0, 5))

    # Load data from DataFrame
    # data = Dataset.load_from_df(reviews_df, reader)

    # Now you can use train_test_split with the Dataset object
    # trainset, testset = train_test_split(data, test_size=0.2)
    # Use user_based true/false to switch between user-based or item-based collaborative filtering
    # algo = KNNWithMeans(
    #     k=5, sim_options={'name': 'pearson_baseline', 'user_based': False})
    # algo.fit(trainset)
    # test_pred = algo.test(testset)
    # print(test_pred)
    # print("Item-based Model : Test Set")
    # accuracy.rmse(test_pred, verbose=True)

# --------------------------------------------
# part3
    new_df1 = reviews_df.head(100000000)
    ratings_matrix = new_df1.pivot_table(
        values='rate', index='user_id', columns='product_id', fill_value=0)
    # print(ratings_matrix.head())
    # print(ratings_matrix.shape)
    X = ratings_matrix.T
    # print(X.head())
    X1 = X
    # Decomposing the Matrix

    SVD = TruncatedSVD(n_components=4)
    decomposed_matrix = SVD.fit_transform(X)
    # print(decomposed_matrix.shape)
    # Correlation Matrix
    correlation_matrix = np.corrcoef(decomposed_matrix)

    recently_activate = UserInfo.objects.all()
    recently_product = []
    list_set = []
    for i in recently_activate:
        url = i.referrer
        pattern = r'/product/(.+)/$'
        match = re.search(pattern, url)
        if match:
            product_name = match.group(1)
            if product_name not in list_set:
                list_set.append(product_name)
                recently_product.append(Product.objects.get(slug=product_name))
    
    recommend_product = []
    number_recommend = []
    if request.user.is_authenticated:
        user_rate = Review.objects.filter(user_id=request.user)
        for count in user_rate:
            correlation_product_ID = correlation_matrix[count.product.count]
            print(correlation_product_ID.shape)
            # Recommending top 25 highly correlated products in sequence
            Recommend = list(X.index[correlation_product_ID > 0.65])
            for j in Recommend[0:10]:
                number_recommend.append(j)
        for i in set(number_recommend):
            recommend_product.append(Product.objects.get(id=i))
    for count in recently_product:
        correlation_product_ID = correlation_matrix[count.count]
        print(correlation_product_ID.shape)
        # Recommending top 25 highly correlated products in sequence
        Recommend = list(X.index[correlation_product_ID > 0.65])
        for j in Recommend[0:10]:
            number_recommend.append(j)
    for i in set(number_recommend):
        recommend_product.append(Product.objects.get(id=i))
    print(recommend_product)
    print(len(recommend_product))
    return HttpResponse("GOOD")
