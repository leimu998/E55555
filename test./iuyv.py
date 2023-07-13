#1. 高斯噪声（gaussian noise）
def add_gaussian_noise(image, mean=0, sigma=30):
    image_np = np.array(image)
    gauss = np.random.normal(mean, sigma, image_np.shape)
    noisy_image = np.clip(image_np + gauss, 0, 255).astype('uint8')
    return Image.fromarray(noisy_image)
# def add_gaussian_noise(image, mean=0, sigma=20):
#     gauss = np.random.normal(mean, sigma, image.size)
#     gauss = gauss.reshape(image.size[1], image.size[0], -1).astype('uint8')
#     noisy_image = Image.fromarray(np.clip(image + gauss, 0, 255))
#     return noisy_image
#2. 椒盐噪声（Salt and Pepper Noise）

def add_salt_pepper_noise(image, prob=0.02):
    image_np = np.array(image)
    shape = image_np.shape
    salt = np.random.choice([0, 1], size=shape, p=[1-prob, prob])
    pepper = np.random.choice([0, 1], size=shape, p=[1-prob, prob])

    salt_noise = np.where(salt == 1, 255, image_np)
    salt_pepper_noise = np.where(pepper == 1, 0, salt_noise)

    return Image.fromarray(salt_pepper_noise)

#3. 泊松噪声（Poisson Noise）
def add_poisson_noise(image, lam=40):
    image_np = np.array(image)
    noise = np.random.poisson(lam, image_np.shape)
    noisy_image = image_np + noise
    return Image.fromarray(np.clip(noisy_image, 0, 255).astype('uint8'))


#4.斑点噪声（Speckle Noise）
def add_speckle_noise(image, mean=0, sigma=0.3):
    image_np = np.array(image)
    speckle = np.random.randn(*image_np.shape) * sigma
    noisy_image = image_np + image_np * speckle
    return Image.fromarray(np.clip(noisy_image, 0, 255).astype('uint8'))
