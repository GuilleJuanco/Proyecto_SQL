#Importar librerías.
import pandas as pd
import numpy as np

#Importa archivo csv para tabla actor y lo añade a DataFrame.
df_actor = pd.read_csv('../data/actor.csv')

#Cuenta nulos.
actor_null = df_actor.isnull().sum()

#Cuenta duplicados.
actor_duplicate = df_actor.duplicated().sum()

#Printea nulos.
print(actor_null) #0 nulos

#Printea dupiclados.
print(actor_duplicate) #0 nulos

#Tira la columna last_update ya que todos los valores son iguales
df_actor.drop('last_update', axis=1, inplace=True)

#Printea df sin columna last_update
display(df_actor)

#Importa archivo csv para tabla category y lo añade a DataFrame.
df_category = pd.read_csv('../data/category.csv')

#Cuenta nulos.
category_null = df_category.isnull().sum()

#Cuenta duplicados.
category_duplicate = df_category.duplicated().sum()

#Printea nulos.
print(category_null) #0 nulos

#Printea dupiclados.
print(category_duplicate) #0 nulos

#Tira la columna last_update ya que todos los valores son iguales
df_category.drop('last_update', axis=1, inplace=True)

#Printea df sin columna last_update
display(df_category)

#Importa archivo csv para tabla category y lo añade a DataFrame.
df_film = pd.read_csv('../data/film.csv')

#Cuenta nulos.
film_null = df_film.isnull().sum()

#Cuenta duplicados.
film_duplicate = df_film.duplicated().sum()

#Printea nulos.
print(film_null) #0 nulos

#Printea dupiclados.
print(film_duplicate) #0 nulos

#Tira la columna last_update ya que todos los valores son iguales
df_film.drop('last_update', axis=1, inplace=True)

#Tira la columna last_update ya que todos los valores son iguales
df_film.drop('original_language_id', axis=1, inplace=True)

#Printea df sin columna last_update ni original_language_id
display(df_film)

#Importa archivo csv para tabla category y lo añade a DataFrame.
df_inventory = pd.read_csv('../data/inventory.csv')

#Cuenta nulos.
inventory_null = df_inventory.isnull().sum()

#Cuenta duplicados.
inventory_duplicate = df_inventory.duplicated().sum()

#Printea nulos.
print(inventory_null) #0 nulos

#Printea dupiclados.
print(inventory_duplicate) #0 nulos

#Tira la columna last_update ya que todos los valores son iguales
df_inventory.drop('last_update', axis=1, inplace=True)

#Printea df sin columna last_update
display(df_inventory)

#Importa archivo csv para tabla category y lo añade a DataFrame.
df_language = pd.read_csv('../data/language.csv')

#Cuenta nulos.
language_null = df_language.isnull().sum()

#Cuenta duplicados.
language_duplicate = df_language.duplicated().sum()

#Printea nulos.
print(language_null) #0 nulos

#Printea dupiclados.
print(language_duplicate) #0 nulos

#Tira la columna last_update ya que todos los valores son iguales
df_language.drop('last_update', axis=1, inplace=True)

#Printea df sin columna last_update
display(df_language)

#Importa archivo csv para tabla category y lo añade a DataFrame.
df_old = pd.read_csv('../data/old_HDD.csv')

#Cuenta nulos.
old_null = df_old.isnull().sum()

#Cuenta duplicados.
old_duplicate = df_old.duplicated().sum()

#Printea nulos.
print(old_null) #0 nulos

#Printea dupiclados.
print(old_duplicate) #0 nulos

#Printea df.
display(df_old)

#Importa archivo csv para tabla category y lo añade a DataFrame.
df_rental = pd.read_csv('../data/rental.csv')

#Cuenta nulos.
rental_null = df_rental.isnull().sum()

#Cuenta duplicados.
rental_duplicate = df_rental.duplicated().sum()

#Printea nulos.
print(rental_null) #0 nulos

#Printea dupiclados.
print(rental_duplicate) #0 nulos

#Tira la columna last_update ya que todos los valores son iguales
df_rental.drop('last_update', axis=1, inplace=True)

#Printea df sin columna last_update
display(df_rental)