from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.setWindowTitle("Estilo com CSS")
window.setStyleSheet("""
    QWidget {
        background-color: #2E3440;
    }
    QPushButton {
        background-color: #88C0D0;
        color: #2E3440;
        font-size: 14px;
        border-radius: 8px;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #81A1C1;
    }
""")

layout = QVBoxLayout()
btn = QPushButton("Clique Aqui")
layout.addWidget(btn)
window.setLayout(layout)
window.show()
app.exec()
