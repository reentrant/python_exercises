def minimal_number_of_packages(items, available_large_packages, available_small_packages):
    large_packages_capacity = 5
    small_packages_capacity = 1
    large_packages = 0
    small_packages = 0
    while items > large_packages_capacity and large_packages<available_large_packages:
        large_packages += 1
        items -= large_packages_capacity
    print(items)
    while items >= small_packages_capacity and small_packages<available_small_packages:
        small_packages += 1
        items -= small_packages_capacity
    return large_packages + small_packages

print(minimal_number_of_packages(16, 2, 10))
