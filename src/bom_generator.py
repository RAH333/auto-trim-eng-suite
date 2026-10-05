"""
This module tracks and organizes the interior or exterior components into a structural manufacturing spreadsheet layout.
"""




"""
Automotive Engineering BOM Generator Module.
"""
from tabulate import tabulate

class BillOfMaterials:
    def __init__(self):
        self.items = []

    def add_component(self, part_number: str, description: str, material: str, weight_kg: float, quantity: int):
        self.items.append({
            "Part Number": part_number,
            "Description": description,
            "Material": material,
            "Weight (kg)": weight_kg,
            "Qty": quantity
        })

    def generate_report(self) -> str:
        if not self.items:
            return "BOM is empty."
        return tabulate(self.items, headers="keys", tablefmt="grid")
      
