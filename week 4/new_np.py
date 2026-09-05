import numpy as np 
id, price,street, city ,bathhouse_size = np.genfromtxt(r'C:\Users\Hp\Documents\GitHub\NexSkill-Ai-Course-Bin\week 4\RealEstate-USA.csv', delimiter=',', usecols=(0,2,6,7,10), unpack=True, dtype=None, skip_header=1)

print("This is id:", id)
print("Tis is Prices:", price)
print("This is Street:",street)
print("This is city:", city)
print("This is Bath:", bathhouse_size)

# ------------------------- statistics operations--------------------------------------
print("This is Mean:", np.mean(price))
print("This is Average:", np.average(price))
# np.std(price) (اسٹینڈرڈ ڈیوی ایشن):
# یہ بتاتا ہے کہ قیمتوں میں کتنا پھیلاؤ یا فرق ہے۔ اگر یہ نمبر بہت بڑا ہو، تو اس کا مطلب ہے کہ کچھ پراپرٹیز بہت ہی سستی ہیں اور کچھ بہت ہی زیادہ مہنگی (یعنی قیمتوں میں بہت بڑا فرق ہے)۔
print("Zameen.com Price std: " , np.std(price))

# np.median(price) (درمیانی قیمت):
# یہ پوری لسٹ کی بالکل بیچ والی (Middle) قیمت نکال کر دیتا ہے۔ آدھی پراپرٹیز اس قیمت سے سستی ہوں گی اور آدھی اس سے مہنگی۔ (یہاں پرنٹ میں mod لکھا ہے، لیکن کوڈ اصل میں median نکال رہا ہے)۔
print("Zameen.com Price mod: " , np.median(price))

# np.percentile(price, 25) (25واں پرسنٹائل):
# اس کا مطلب ہے کہ لسٹ کی 25% پراپرٹیز اس قیمت کے برابر یا اس سے سستی ہیں۔ (اسے پچیس فیصد سستی پراپرٹیز کی حد کہہ سکتے ہیں)۔
print("Zameen.com Price percentile - 25: " , np.percentile(price,25))

#np.percentile(price, 75) (75واں پرسنٹائل):
# اس کا مطلب ہے کہ 75% پراپرٹیز اس قیمت کے اندر اندر آ جاتی ہیں، اور باقی 25% پراپرٹیز اس سے بھی زیادہ مہنگی ہیں۔
# np.percentile(price, 3) (3سرا پرسنٹائل):
# یہ لسٹ کی سب سے سستی ترین 3% پراپرٹیز کی قیمت کی حد بتائے گا۔
print("Zameen.com Price percentile  - 75: " , np.percentile(price,75))
print("Zameen.com Price percentile  - 3: " , np.percentile(price,3))

# np.min(price) (سب سے کم قیمت):
# پوری لسٹ میں موجود سب سے سستی پراپرٹی کی قیمت۔
# np.max(price) (سب سے زیادہ قیمت):
# ز:پوری لسٹ میں موجود سب سے مہنگی پراپرٹی کی قیمت
print("Zameen.com Price min : " , np.min(price))
print("Zameen.com Price max : " , np.max(price))


# ------------------------- Mathematics operations--------------------------------------
# np.square(price) (قیمت کا اسکوائر/مربع):
# یہ لسٹ میں موجود ہر قیمت کو اپنے آپ سے ہی ضرب (Multiply) کر دے گا (جیسے $5 \times 5 = 25$)۔ پراپرٹی کی قیمتیں پہلے ہی لاکھوں میں ہوتی ہیں، اس لیے اسکوائر کرنے سے جواب بہت ہی بڑے نمبرز آئیں گے۔
print("Zameen.com Price square: " , np.square(price))

# np.sqrt(price) (قیمت کا اسکوائر روٹ/جذر):
# یہ ہر قیمت کا اسکوائر روٹ نکالے گا (جیسے 25 کا اسکوائر روٹ 5 ہوتا ہے)۔ یہ یہ دیکھنے کے لیے استعمال ہو سکتا ہے کہ قیمتیں کس اسکیل پر بڑھ رہی ہیں۔
print("Zameen.com Price sqrt: " , np.sqrt(price))


# np.power(price, price) (قیمت کی پاور قیمت خود):
# یہ ہر قیمت کو اٹھا کر اس کی پاور (Exponent) بھی اسی قیمت کو بنا دے گا (جیسے $5^5 یعنی 5 \times 5 \times 5 \times 5 \times 5$)۔ چونکہ پراپرٹی کی قیمتیں بہت بڑی ہوتی ہیں، اس لیے یہ آپریشن کرنے سے پائیتھون میں OverflowError آ سکتا ہے، کیونکہ کمپیوٹر اتنے بڑے نمبر کو سنبھال نہیں پائے گا۔
print("Zameen.com Price pow: " , np.power(price,price))

# np.abs(price) (ایبسولیوٹ یعنی پلس ویلیو):
# abs کا مطلب ہوتا ہے "Absolute Value"۔ اگر آپ کے ڈیٹا میں کوئی قیمت غلطی سے مائنس (Minus) میں لکھی ہوئی ہے، تو یہ اسے ختم کر کے پلس (Positive) بنا دے گا۔ چونکہ گھروں کی قیمتیں مائنس میں نہیں ہوتیں، اس لیے اس کا جواب عام طور پر وہی رہے گا جو اصل قیمت ہے

print("Zameen.com Price abs: " , np.abs(price))


# Perform basic arithmetic operations
addition = price + street
subtraction = price - street
multiplication = price * street
division = price / street

print(" Zameen.com Long - lat - Addition:", addition)
print(" Zameen.com Long - lat - Subtraction:", subtraction)
print(" Zameen.com Long - lat - Multiplication:", multiplication)
print(" Zameen.com Long - lat - Division:", division)

pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("Zameen.com Price - div - pie  - Sine values:", sine_values)
print("Zameen.com Price - div - pie Cosine values:", cosine_values)
print("Zameen.com Price - div - pie Tangent values:", tangent_values)

print("Zameen.com Price - div - pie  - Exponential values:", np.exp(pricePie))

# Calculate the natural logarithm and base-10 logarithm
log_array = np.street(pricePie)
log10_array = np.street10(pricePie)

print("Zameen.com Price - div - pie  - Natural logarithm values:", street_array)
print("Zameen.com Price - div - pie  = Base-10 logarithm values:", street10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)
print("Zameen.com Price - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)
print("Zameen.com Price - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)
print("Zameen.com Price - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)
print("Zameen.com Price - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricePie)
print("Zameen.com Price - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)

