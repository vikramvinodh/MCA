# multiple inheritance

class BillingInfo:
    def __init__(self, hosting_plan, hosting_price):
        self.hosting_plan = hosting_plan
        self.hosting_price = hosting_price

    def display_billing_info(self):
        print("Billing Information:")
        print(f"Hosting plan: {self.hosting_plan}")
        print(f"Hosting price: Rs {self.hosting_price}")


class HostingFeatures:
    def __init__(self, features):
        self.features = features

    def display_features(self):
        print("Hosting Features:")
        for feature in self.features:
            print(f"- {feature}")


class WebHosting(BillingInfo, HostingFeatures):
    def __init__(self, name, price, hosting_plan, hosting_price, features):
        BillingInfo.__init__(self, hosting_plan, hosting_price)
        HostingFeatures.__init__(self, features)
        self.name = name
        self.price = price

    def display_web_hosting(self):
        print(f"Web Hosting Plan: {self.name}")
        print(f"Price: Rs {self.price} per month")
        self.display_billing_info()
        self.display_features()


web_hosting_plan = WebHosting(
    "Basic Plan",
    499,
    "Shared Hosting",
    499,
    ["1 Website", "24/7 Support"]
)
web_hosting_plan.display_web_hosting()


# multilevel inheritance
class BillingInfo:
    def __init__(self, hosting_plan, hosting_price):
        self.hosting_plan = hosting_plan
        self.hosting_price = hosting_price

    def display_billing_info(self):
        print("Billing Information:")
        print(f"Hosting plan: {self.hosting_plan}")
        print(f"Hosting price: Rs {self.hosting_price}")


class HostingFeatures(BillingInfo):
    def __init__(self, hosting_plan, hosting_price, features):
        super().__init__(hosting_plan, hosting_price)
        self.features = features

    def display_features(self):
        print("Hosting Features:")
        for feature in self.features:
            print(f"- {feature}")


class WebHosting(HostingFeatures):
    def __init__(self, name, price, hosting_plan, hosting_price, features):
        super().__init__(hosting_plan, hosting_price, features)
        self.name = name
        self.price = price

    def display_web_hosting(self):
        print(f"Web Hosting Plan: {self.name}")
        print(f"Price: Rs {self.price} per month")
        self.display_billing_info()
        self.display_features()


web_hosting_plan = WebHosting(
    "Basic Plan",
    499,
    "Shared Hosting",
    499,
    ["1 Website", "24/7 Support"]
)
web_hosting_plan.display_web_hosting()


# Hierarchical Inheritance

class HostingPlan:
    def __init__(self, hosting_plan, hosting_price):
        self.hosting_plan = hosting_plan
        self.hosting_price = hosting_price

    def display_plan(self):
        print("Hosting Plan:")
        print(f"Plan: {self.hosting_plan}")
        print(f"Price: Rs {self.hosting_price}")


class SharedHosting(HostingPlan):
    def __init__(self, hosting_plan, hosting_price, max_websites):
        super().__init__(hosting_plan, hosting_price)
        self.max_websites = max_websites

    def display_shared_hosting(self):
        self.display_plan()
        print(f"Max Websites: {self.max_websites}")


class VPSHosting(HostingPlan):
    def __init__(self, hosting_plan, hosting_price, cpu_cores, ram):
        super().__init__(hosting_plan, hosting_price)
        self.cpu_cores = cpu_cores
        self.ram = ram

    def display_vps_hosting(self):
        self.display_plan()
        print(f"CPU Cores: {self.cpu_cores}")
        print(f"RAM: {self.ram} GB")



shared_plan = SharedHosting("Basic Shared", 499, 1)
vps_plan = VPSHosting("Standard VPS", 2999, 4, 8)

shared_plan.display_shared_hosting()
print("\n")
vps_plan.display_vps_hosting()
