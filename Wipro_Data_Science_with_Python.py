{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMA4z7kI0EI6z7Xd7cxMLoh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/raghavsahu511/JavaScript-projects/blob/main/Wipro_Data_Science_with_Python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Pyhton Fundamentals**"
      ],
      "metadata": {
        "id": "MAhsCz06YOkS"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Hands on Assignment on Flow Control Statements*\n"
      ],
      "metadata": {
        "id": "wzZj9lfJXgVt"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "1.   WAP to check if a given No. is +ve , -ve or 0.\n",
        "\n"
      ],
      "metadata": {
        "id": "6P81xU7BYHVg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "n = float(input(\"Enter a number: \"))\n",
        "if n > 0:\n",
        "   print(\"Positive number\")\n",
        "elif n == 0:\n",
        "   print(\"Zero\")\n",
        "else:\n",
        "   print(\"Negative number\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DmEYqqvAZxnL",
        "outputId": "5440d825-2d6d-491a-d267-d9a0b25b60a6"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 6\n",
            "Positive number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. WAP to check if a given No. is odd or even."
      ],
      "metadata": {
        "id": "Yfqmj6rgaEah"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "n = float(input(\"Enter a number: \"))\n",
        "if n%2==0:\n",
        "  print(\"Even number\")\n",
        "else:\n",
        "  print(\"Odd number\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jGudwKypaZFf",
        "outputId": "1c941511-ca27-4038-e01d-f5374ffcf8fc"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 4\n",
            "Even number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.\n",
        "\n",
        "\n",
        "*   lastDigit(7,17) -> true\n",
        "*   lastDigit(6,17) -> false\n",
        "\n",
        "*   lastDigit(3,113) -> true\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "34OUTTc3am2c"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = int(input(\"Enter the first non-negative number: \"))\n",
        "num2 = int(input(\"Enter the second non-negative number: \"))\n",
        "\n",
        "last_digit_num1 = num1 % 10\n",
        "last_digit_num2 = num2 % 10\n",
        "\n",
        "if (last_digit_num1 == last_digit_num2):\n",
        "    print(\"True\")\n",
        "else:\n",
        "    print(\"False\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XcRvfD3wbmfr",
        "outputId": "25cffeab-e9dd-45bc-d71a-82db9a962c20"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the first non-negative number: 5\n",
            "Enter the second non-negative number: 15\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. WAP to print no.s from 1 to 10 in a single row with one tab space.\n"
      ],
      "metadata": {
        "id": "3thrtSiACwkr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,11):\n",
        "  print(i, end = '\\t')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WdXX-u2RD7Ea",
        "outputId": "00e688d2-5e63-486e-bfc7-7ea17647cd7d"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. WAP to print even no.s from 23 and 57. Each no. should be printed in a separate row."
      ],
      "metadata": {
        "id": "RgGUvapfEMCK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(23, 58):\n",
        "  if i % 2 == 0:\n",
        "    print(i, end = '\\n' )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zJeuWbi7El7M",
        "outputId": "24742aca-dfb6-489d-e721-14ef1d712a33"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "24\n",
            "26\n",
            "28\n",
            "30\n",
            "32\n",
            "34\n",
            "36\n",
            "38\n",
            "40\n",
            "42\n",
            "44\n",
            "46\n",
            "48\n",
            "50\n",
            "52\n",
            "54\n",
            "56\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6. WAP to check if a given no. is prime or not."
      ],
      "metadata": {
        "id": "xXLwAbfQFC2F"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = int(input(\"Enter a number: \"))\n",
        "\n",
        "if a <= 1:\n",
        "    print(a, \"is not a prime number\")\n",
        "elif a == 2:\n",
        "    print(a, \"is a prime number\")\n",
        "else:\n",
        "    is_prime = True\n",
        "    for i in range(2, int(a**0.5) + 1):\n",
        "        if (a % i) == 0:\n",
        "            is_prime = False\n",
        "            break\n",
        "    if is_prime:\n",
        "        print(a, \"is a prime number\")\n",
        "    else:\n",
        "        print(a, \"is not a prime number\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hZS5DG8wF_3k",
        "outputId": "6dc948bf-e49a-4451-cef8-0a5d0d9a3692"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 8\n",
            "8 is not a prime number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "7. WAP to print prime no.s between 10 and 99."
      ],
      "metadata": {
        "id": "dXEGsnmOGVWz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(10, 100):\n",
        "  if i > 1:\n",
        "    for j in range(2, i):\n",
        "      if i % j == 0:\n",
        "        break\n",
        "    else:\n",
        "      print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tP1r7wNKGoRZ",
        "outputId": "91af520e-9dda-4478-c0a7-6726b3ff36f8"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "11\n",
            "13\n",
            "17\n",
            "19\n",
            "23\n",
            "29\n",
            "31\n",
            "37\n",
            "41\n",
            "43\n",
            "47\n",
            "53\n",
            "59\n",
            "61\n",
            "67\n",
            "71\n",
            "73\n",
            "79\n",
            "83\n",
            "89\n",
            "97\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "8. WAP to print the sum of all the digits of a given number. Ex: I/P = 1234  O/P = 10"
      ],
      "metadata": {
        "id": "gPs7PN5LHIQM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input(\"Enter a number: \"))\n",
        "sum_digits = 0\n",
        "while num > 0:\n",
        "    digit = num % 10\n",
        "    sum_digits += digit\n",
        "    num = num // 10\n",
        "print(\"Sum of digits =\", sum_digits)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "js0NcYlcNp1l",
        "outputId": "43eef6ea-1e41-4654-d2e4-41364389fcec"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 1234\n",
            "Sum of digits = 10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "9. WAP to reverse a given no. and print.\n",
        "\n",
        "*   Ex 1: I/P = 1234  O/P = 4321\n",
        "*   Ex 2: I/P = 1004  O/P = 4001\n",
        "\n"
      ],
      "metadata": {
        "id": "5Y2T7fQXN-FJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input(\"Enter a number: \"))\n",
        "rev_num = 0\n",
        "while num > 0:\n",
        "    digit = num % 10\n",
        "    rev_num = rev_num * 10 + digit\n",
        "    num = num // 10\n",
        "\n",
        "print(\"Reversed number: \",rev_num)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d4uRp6HrPj02",
        "outputId": "5a70b094-4448-4353-dd08-589e31f04ce8"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 1004\n",
            "Reversed number:  4001\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "10. WAP to find if the given number is palindrome or not\n",
        "\n",
        "\n",
        "*   Ex 1: I/P = 110011  O/P = 110011 is a palindrome.\n",
        "*   Ex 2: I/P = 1234  O/P = 1234 is not a palindrome.\n",
        "\n"
      ],
      "metadata": {
        "id": "wmh6w-yiRMp3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input(\"Enter a number: \"))\n",
        "\n",
        "original = num\n",
        "reverse = 0\n",
        "\n",
        "while num > 0:\n",
        "    digit = num % 10\n",
        "    reverse = reverse * 10 + digit\n",
        "    num = num // 10\n",
        "\n",
        "if original == reverse:\n",
        "    print(original, \"is a palindrome.\")\n",
        "else:\n",
        "    print(original, \"is not a palindrome.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xCfyNhtLTvBz",
        "outputId": "e973c9f0-3132-473e-f9ed-335182b37a33"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 110011\n",
            "110011 is a palindrome.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *MINI-PROJECTS*"
      ],
      "metadata": {
        "id": "jf1nltEjUZtU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        " PROJECT- 1  => Create a python program that asks the user how far they want to travel. If they want to travel 3 miles : Bicycle , 3 to 300 miles : Motor-cycle , 300 miles or more : Super-Car.\n",
        " Sample Output = How far would you like to travel in miles ? 2500\n",
        " I suggest Super-Car to your destination"
      ],
      "metadata": {
        "id": "crI6Za36UkWO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Dist = float(input(\"How far would you like to travel in miles ? \"))\n",
        "if Dist <= 3:\n",
        "  print(\"I suggest Bicycle to your destination\")\n",
        "elif Dist > 3 and Dist <= 300:\n",
        "  print(\"I suggest Motor-cycle to your destination\")\n",
        "else:\n",
        "  print(\"I suggest Super-Car to your destination\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nfiKyXflaCG4",
        "outputId": "c11790f6-f8e6-4b00-c561-f2a081ff9d9a"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "How far would you like to travel in miles ? 2500\n",
            "I suggest Super-Car to your destination\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "PROJECT- 2 => Let's assume you ---- PBLApp for Mobile. You ----- charges $0.51 per hour. You ----- month.\n",
        "WAP in python that displays answers to the following Qs.\n",
        "\n",
        "*   How much does it cost to operate one server per day?\n",
        "*   How much does it cost to operate one server per week?\n",
        "\n",
        "\n",
        "*   How much does it cost to operate one server per month?\n",
        "*   How many days can I operate one server with $918?\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "8dj44GGWahk0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cost_per_hour = 0.51\n",
        "\n",
        "# Cost to operate one server per day\n",
        "cost_per_day = cost_per_hour * 24\n",
        "print(f\"Cost to operate one server per day: ${cost_per_day:.2f}\")\n",
        "\n",
        "# Cost to operate one server per week\n",
        "cost_per_week = cost_per_day * 7\n",
        "print(f\"Cost to operate one server per week: ${cost_per_week:.2f}\")\n",
        "\n",
        "# Cost to operate one server per month (assuming 30 days in a month)\n",
        "cost_per_month = cost_per_day * 30\n",
        "print(f\"Cost to operate one server per month: ${cost_per_month:.2f}\")\n",
        "\n",
        "# How many days can I operate one server with $918?\n",
        "budget = 918\n",
        "days_of_operation = budget / cost_per_day\n",
        "print(f\"With ${budget}, you can operate one server for {days_of_operation:.2f} days.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KILImWjeczKY",
        "outputId": "05b82b33-f013-43df-91b4-9cc07c506125"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cost to operate one server per day: $12.24\n",
            "Cost to operate one server per week: $85.68\n",
            "Cost to operate one server per month: $367.20\n",
            "With $918, you can operate one server for 75.00 days.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Data Structures**"
      ],
      "metadata": {
        "id": "3bqwuEDg14fU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Hands on Assignment on List*"
      ],
      "metadata": {
        "id": "r2EpdAs3drF2"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. WAP to create a list of 5 integers and display the list items. Access individual elements through index."
      ],
      "metadata": {
        "id": "5SjRoR_dj5UF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Li = [11,22,33,44,55]\n",
        "print(\"The list is:\", Li)\n",
        "print(\"First element (index 0):\", Li[0])\n",
        "print(\"Second element (index 1):\", Li[1])\n",
        "print(\"Third element (index 2):\", Li[2])\n",
        "print(\"Fourth element (index 3):\", Li[3])\n",
        "print(\"Fifth element (index 4):\", Li[4])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GoIXc88qlGKU",
        "outputId": "f82fdfa0-2952-493a-a391-0a42adcd0692"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The list is: [11, 22, 33, 44, 55]\n",
            "First element (index 0): 11\n",
            "Second element (index 1): 22\n",
            "Third element (index 2): 33\n",
            "Fourth element (index 3): 44\n",
            "Fifth element (index 4): 55\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. WAP to append a new item to the end of the list."
      ],
      "metadata": {
        "id": "h1j8JuVVlRc0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "my_List = [1, 2, 3]\n",
        "new_item = 4\n",
        "my_List.append(new_item)\n",
        "print(my_List)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WlKyAwvflfYr",
        "outputId": "ef58fafc-0435-4f49-d98c-d11df73022e8"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. WAP to reverse the order of items in the list."
      ],
      "metadata": {
        "id": "WulM08tvl2xb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Li = [\"Rahul\",8,5,\"Ross\"]\n",
        "Li_new = Li[::-1]\n",
        "print(\"Reversed List: \",Li_new)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WhOEnm7DmNQf",
        "outputId": "40ed627c-7fea-43b5-dd1a-f32d3ccca909"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reversed List:  ['Ross', 5, 8, 'Rahul']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. WAP to print the no. of occurences of a specified element in a list."
      ],
      "metadata": {
        "id": "T4zBL3-uOzR3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "my_list = [1,2,2,3,4,2,5,6,2]\n",
        "element_to_find = int(input(\"Enter the element to count: \"))\n",
        "occurrences = my_list.count(element_to_find)\n",
        "print(f\"The element {element_to_find} appears {occurrences} times in the list.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KIhiA1wnP3RC",
        "outputId": "afe98e54-e5d6-4ba1-8908-16775d6fa230"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the element to count: 2\n",
            "The element 2 appears 4 times in the list.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. WAP to append the items of list1 to list2 in the front."
      ],
      "metadata": {
        "id": "BrSe6gWWQdpF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "list1 = [\"Alex\",\"Root\",\"Eoin\"]\n",
        "list2 = [1,2,3,4]\n",
        "# Append items of list2 to the front of list1\n",
        "list2[:0] = list1\n",
        "print(\"New List: \",list2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "laaLZ6WBSECk",
        "outputId": "d3dfcf40-3d20-44be-81b0-ebfdf60aeed3"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "New List:  ['Alex', 'Root', 'Eoin', 1, 2, 3, 4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6. WAP to insert a new item before the second element in an existing list."
      ],
      "metadata": {
        "id": "yihaCucrSRSK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "List = [3,4,5,6,7]\n",
        "List.insert(1,10)\n",
        "print(\"New List: \",List)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7ZL0H8EVTwZt",
        "outputId": "9c4aa488-8404-4368-ae84-6cd77ede7cd3"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "New List:  [3, 10, 4, 5, 6, 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "7. WAP to remove the item from a specified index in a list."
      ],
      "metadata": {
        "id": "RNOanXQmUN4U"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "my_List = [10,20,30,40,50]\n",
        "my_List.remove(20)\n",
        "print(\"New List: \",my_List)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "55UhKSjtVnMh",
        "outputId": "a293fb85-b034-4412-c0dc-7bfbb93c3e02"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "New List:  [10, 30, 40, 50]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "8. WAP to remove the first occurence of a specified element from a list."
      ],
      "metadata": {
        "id": "FTxYtUIkWYw3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "lst = [10, 20, 30, 20, 40, 50]\n",
        "x = int(input(\"Enter the element to remove: \"))\n",
        "if x in lst:\n",
        "    lst.remove(x)      # removes only the first occurrence\n",
        "    print(\"Updated List:\", lst)\n",
        "else:\n",
        "    print(\"Element not found\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8O4r1ps_WoBD",
        "outputId": "f1fcf1a0-2419-4f4e-8ec1-6de5900b0d39"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the element to remove: 30\n",
            "Updated List: [10, 20, 20, 40, 50]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Hands on Assignment on Dictionary*"
      ],
      "metadata": {
        "id": "87JyShN0XDlA"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. WAP to add akey and value to a dictionary.\n",
        "Sample Dictionary : {0:10, 1:20}\n",
        "Expected Result : {0:10, 1:20, 2:30}"
      ],
      "metadata": {
        "id": "YM9HG8Woem9T"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dict_1 = {0:10, 1:20}\n",
        "dict_1[2] = 30\n",
        "print(\"New Dictionary: \",dict_1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1mVkkiPWfYrO",
        "outputId": "d87bb0be-9452-4694-d6ae-8a9c367e375c"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "New Dictionary:  {0: 10, 1: 20, 2: 30}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. WAP to concatenate the following dictionaries to create a new one.\n",
        "Sample Dictionary : dic1={1:10,2:20} dic2={3:30,4:40} dic3={5:50,6:60}   Expected Result : {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}"
      ],
      "metadata": {
        "id": "rMjLFqizgkAj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dic1 = {1:10, 2:20}\n",
        "dic2 = {3:30, 4:40}\n",
        "dic3 = {5:50, 6:60}\n",
        "dic1.update(dic2)\n",
        "dic1.update(dic3)\n",
        "print(\"New Dictionary: \",dic1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m9hPHCSwiI7B",
        "outputId": "0a713f5a-4a2d-48a1-8ce4-aa4ef9145e51"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "New Dictionary:  {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. WAP to check if a given key already exists in a dictionary."
      ],
      "metadata": {
        "id": "C0QCjT8Sjhxd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}\n",
        "key_to_check = input(\"Enter a key to check: \")\n",
        "if key_to_check in my_dict:\n",
        "    print(f\"The key '{key_to_check}' exists in the dictionary.\")\n",
        "else:\n",
        "    print(f\"The key '{key_to_check}' does not exist in the dictionary.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wExjVRfwkMeO",
        "outputId": "2d03c8ba-291b-4dfa-a1c5-c5564fe5d842"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a key to check: apple\n",
            "The key 'apple' exists in the dictionary.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. WAP to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values."
      ],
      "metadata": {
        "id": "Wjssuyf3kYBd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}\n",
        "print(\"Keys:\")\n",
        "for key in my_dict:\n",
        "    print(key)\n",
        "print(\"\\nValues:\")\n",
        "for value in my_dict.values():\n",
        "    print(value)\n",
        "print(\"\\nKey-Value Pairs:\")\n",
        "for key, value in my_dict.items():\n",
        "    print(f\"{key}: {value}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mFD-Q9evl09l",
        "outputId": "18551b2c-5687-476b-b6e9-d8488d5942b5"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Keys:\n",
            "apple\n",
            "banana\n",
            "cherry\n",
            "\n",
            "Values:\n",
            "1\n",
            "2\n",
            "3\n",
            "\n",
            "Key-Value Pairs:\n",
            "apple: 1\n",
            "banana: 2\n",
            "cherry: 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. WAP to prepare a dictionary where the keys are numbers b/w 1 and 15 (both included) and the values are square of the keys."
      ],
      "metadata": {
        "id": "wHplgI76mAeC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Dictionary: \")\n",
        "for i in range(1,16):\n",
        "  print(f\"{i}: {i*i}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x6C6hKtlnuyc",
        "outputId": "46d4d761-491a-4d0d-ae72-a13a5c65403a"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dictionary: \n",
            "1: 1\n",
            "2: 4\n",
            "3: 9\n",
            "4: 16\n",
            "5: 25\n",
            "6: 36\n",
            "7: 49\n",
            "8: 64\n",
            "9: 81\n",
            "10: 100\n",
            "11: 121\n",
            "12: 144\n",
            "13: 169\n",
            "14: 196\n",
            "15: 225\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6. WAP to sum all the values in a dictionary, considering the values will be of int type.  "
      ],
      "metadata": {
        "id": "QSlWq8g_pB0L"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}\n",
        "total_sum_loop = 0\n",
        "for value in my_dict.values():\n",
        "    total_sum_loop += value\n",
        "print(f\"Sum using loop: {total_sum_loop}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DWi3PamcqBnK",
        "outputId": "b292c69b-5121-476e-c289-317d575b6fec"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sum using loop: 100\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Hands on Assignment on Tuple*"
      ],
      "metadata": {
        "id": "Iy5jU1rxqNU8"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. WAP to print the 4th element from first and 4th element from last in a tuple."
      ],
      "metadata": {
        "id": "NVjIa4VzqdwB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)\n",
        "first_fourth_element = my_tuple[3]\n",
        "last_fourth_element = my_tuple[-4]\n",
        "print(f\"4th element from the first: {first_fourth_element}\")\n",
        "print(f\"4th element from the last: {last_fourth_element}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jT0m9e02sVWx",
        "outputId": "c310783c-9df0-47f8-dba9-bbccd0f2232f"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4th element from the first: 40\n",
            "4th element from the last: 70\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. WAP to check whether an element exists in a tuple or not."
      ],
      "metadata": {
        "id": "H0FrEbbSshUi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tup = (1,2,3,4,5)\n",
        "element = int(input(\"Enter an element to check: \"))\n",
        "if element in tup:\n",
        "  print(f\"{element} exists in the tuple.\")\n",
        "else:\n",
        "  print(f\"{element} does not exist in the tuple.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iLrQI0KOq7a1",
        "outputId": "51d421a9-2320-436e-96db-6c4bcde25d1b"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter an element to check: 3\n",
            "3 exists in the tuple.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. WAP to convert a list into a tuple."
      ],
      "metadata": {
        "id": "9JEWZZvLs8hM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "List = [1,2,3,4,5]\n",
        "Tuple = tuple(List)\n",
        "print(\"Tuple: \",Tuple)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UcvJiH52tMcb",
        "outputId": "7ce18982-67ea-48b7-a899-bc13b6423a1b"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Tuple:  (1, 2, 3, 4, 5)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. WAP to find the index of an item in a tuple."
      ],
      "metadata": {
        "id": "8jYY4MSutsTD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tup = (10, 20, 30, 40, 50)\n",
        "item = int(input(\"Enter the item to find: \"))\n",
        "if item in tup:\n",
        "    print(\"Index:\", tup.index(item))\n",
        "else:\n",
        "    print(\"Item not found\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cz6Wj8eWySsh",
        "outputId": "c375b08a-f471-43e6-fc87-9ab45c52ec4b"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the item to find: 20\n",
            "Index: 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. WAP to replace last value of tuples in a list to 100.\n",
        "Sample List: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]\n",
        "Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]"
      ],
      "metadata": {
        "id": "73bnfl2hybG0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Li = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]\n",
        "result = []\n",
        "for tup in Li:\n",
        "    result.append(tup[:-1] + (100,))\n",
        "print(result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lz4UxaB10UzJ",
        "outputId": "9b27b7b9-cdad-40a6-8274-37e42f11fd88"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[(10, 20, 100), (40, 50, 100), (70, 80, 100)]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Hands on Assignment on Set*"
      ],
      "metadata": {
        "id": "kcqmUGkA1SEL"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. WAP to remove a given item from the set."
      ],
      "metadata": {
        "id": "ML3viN5G1tih"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "set1 = {1, 2, 3, 4, 5}\n",
        "item_to_remove = int(input(\"Enter the item to remove: \"))\n",
        "if item_to_remove in set1:\n",
        "    set1.remove(item_to_remove)\n",
        "print(\"Updated Set:\", set1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bGutwOsV3Ci9",
        "outputId": "2504f11c-2102-417b-8761-d3bf6bee6e44"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the item to remove: 4\n",
            "Updated Set: {1, 2, 3, 5}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. WAP to create an intersection of sets."
      ],
      "metadata": {
        "id": "_6NtD0U43QBP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "set1 = {1, 2, 3, 4, 5}\n",
        "set2 = {4, 5, 6, 7, 8}\n",
        "new_set = set1.intersection(set2)\n",
        "print(\"Intersection of sets:\", new_set)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E8TNG1xdCMjy",
        "outputId": "5d3d42db-b358-423f-e95b-44063730a546"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Intersection of sets: {4, 5}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. WAP to create an union of sets."
      ],
      "metadata": {
        "id": "JdhByYpuCXVv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "set1 = {1, 2, 3, 4, 5}\n",
        "set2 = {4, 5, 6, 7, 8}\n",
        "new_set = set1.union(set2)\n",
        "print(\"Union of sets:\", new_set)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QRJR_3GSCgxo",
        "outputId": "b3d57a62-076d-4e6b-e284-e4c2b3718cab"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Union of sets: {1, 2, 3, 4, 5, 6, 7, 8}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. WAP to find the maximum and minimum value in a set."
      ],
      "metadata": {
        "id": "7KzsMhouCqcq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "set1 = {1, 2, 3, 4, 5}\n",
        "print(\"Maximum value of set: \", max(set1))\n",
        "print(\"Minimum value of set: \", min(set1))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dzgs9gLdC4I9",
        "outputId": "50567c15-0e0c-47a5-d8b7-de415dc9f334"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Maximum value of set:  5\n",
            "Minimum value of set:  1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Hands on Assignment on String*"
      ],
      "metadata": {
        "id": "grPcb1UKDWFB"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. WAP to count the no. of upper and lower case letters in a string."
      ],
      "metadata": {
        "id": "K4Oa6lPzDnm6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "my_string = input(\"Enter a string: \")\n",
        "upper_count = 0\n",
        "lower_count = 0\n",
        "for char in my_string:\n",
        "    if char.isupper():\n",
        "        upper_count += 1\n",
        "    elif char.islower():\n",
        "        lower_count += 1\n",
        "print(f\"Number of uppercase letters: {upper_count}\")\n",
        "print(f\"Number of lowercase letters: {lower_count}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dtX4tqkdEF7k",
        "outputId": "38afdf40-b328-4334-8665-7d205782b39b"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a string: Hello World\n",
            "Number of uppercase letters: 2\n",
            "Number of lowercase letters: 8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. WAP that will check whether a given string is palindrome or not."
      ],
      "metadata": {
        "id": "wOSeMaVtEZmW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Str = input(\"Enter a string: \")\n",
        "if Str == Str[::-1]:\n",
        "    print(\"Palindrome\")\n",
        "else:\n",
        "    print(\"Not a Palindrome\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WNiQPfm0E3gc",
        "outputId": "03e05f39-91b0-4903-bf86-265806a43402"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a string: BoB\n",
            "Palindrome\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >=2. If input is \"Wipro\" then output should be \"WiWiWiWiWi\"."
      ],
      "metadata": {
        "id": "awQt7vJxFd1y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Str = input(\"Enter a string: \")\n",
        "n = len(Str)\n",
        "if n >= 2:\n",
        "    first_two_chars = Str[:2]\n",
        "    new_string = first_two_chars * n\n",
        "    print(\"New string:\", new_string)\n",
        "else:\n",
        "    print(\"Invalid String\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9fyG1zaGIKE1",
        "outputId": "4d538b9c-b5d1-4ffc-cc14-71f91f903588"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a string: Wipro\n",
            "New string: WiWiWiWiWi\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is \"xHix\", then output is \"Hi\"."
      ],
      "metadata": {
        "id": "T3q9jmwvJ0e9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "S = input(\"Enter a string: \")\n",
        "if S[0] == 'x' or S[-1] == 'x':\n",
        "    new_S = S.replace('x', '')\n",
        "    print(\"New string: \", new_S)\n",
        "else:\n",
        "    print(\"New string: \", S)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QaRRzfzEwUeq",
        "outputId": "c2b23e2e-c7f8-444a-c8b4-ef544624810b"
      },
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a string: xHix\n",
            "New string:  Hi\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is b/w 0 and length of string inclusive. For Example if the inputs are \"Wipro\" and 3, then the output should be \"propropro\"."
      ],
      "metadata": {
        "id": "K4vRLJW4wzRO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "string = input(\"Enter a string: \")\n",
        "n = int(input(\"Enter an integer: \"))\n",
        "if 0 <= n <= len(string):\n",
        "    last_n_chars = string[-n:]\n",
        "    new_string = last_n_chars * n\n",
        "    print(\"New string:\", new_string)\n",
        "else:\n",
        "    print(\"Invalid input for n\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ikt_tKS7x_M8",
        "outputId": "506e8579-94eb-4419-b275-2412b0e3a439"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a string: Wipro\n",
            "Enter an integer: 3\n",
            "New string: propropro\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *MINI-PROJECTS*"
      ],
      "metadata": {
        "id": "7Vpxdl13yXO5"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "PROJECT- 1 => Create a dictionary -----. Display each person and his/her interesting fact to the screen. Next, -------- facts. Run the program multiple times and notice if the order changes.\n",
        "Sample Output =\n",
        "Jeff: Is afraid of Dogs.\n",
        "David: Plays the piano.\n",
        "Jason: Can fly an airplane.\n",
        "\n",
        "Jeff: Is afraid of heights.\n",
        "David: Plays the piano.\n",
        "Jason: Can fly an airplane.\n",
        "Jill: Can hula dance.\n"
      ],
      "metadata": {
        "id": "lJjKsDGOymzG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "facts = {\n",
        "    \"Jeff\": \"Is afraid of Dogs.\",\n",
        "    \"David\": \"Plays the piano.\",\n",
        "    \"Jason\": \"Can fly an airplane.\"\n",
        "}\n",
        "for person, fact in facts.items():\n",
        "    print(f\"{person}: {fact}\")\n",
        "facts[\"Jeff\"] = \"Is afraid of heights.\" # Modify an existing fact\n",
        "facts[\"Jill\"] = \"Can hula dance.\" # Add a new person and their fact\n",
        "print(\"\\nUpdated facts:\")\n",
        "for person, fact in facts.items():\n",
        "    print(f\"{person}: {fact}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EHGTTiVA2A_H",
        "outputId": "be6557a1-7411-4e7a-c195-548cb9871011"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Jeff: Is afraid of Dogs.\n",
            "David: Plays the piano.\n",
            "Jason: Can fly an airplane.\n",
            "\n",
            "Updated facts:\n",
            "Jeff: Is afraid of heights.\n",
            "David: Plays the piano.\n",
            "Jason: Can fly an airplane.\n",
            "Jill: Can hula dance.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "PROJECT- 2 => Given the Participant's Score -------- . You have Scores. Stores them in a list and find the score of the runner-up.\n",
        "**Sample input** : [2, 3, 6, 6, 5]\n",
        "**Sample Output** : 5  (Second Maximum)"
      ],
      "metadata": {
        "id": "zI7jXhQ22wTV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Scores = [2, 3, 6, 6, 5]\n",
        "Sec_max = max(Scores)\n",
        "while max(Scores) == Sec_max:\n",
        "    Scores.remove(max(Scores))\n",
        "print(\"Second Maximum or Runners-up : \",max(Scores))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rYV-kkJf4RPH",
        "outputId": "81dedd66-961f-4194-eec3-1e86cf965ee5"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Second Maximum or Runners-up :  5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "PROJECT- 3 => You have a record of n students. --------- Student's name is key. Marks stored in a list is the value.--------- student.\n",
        "**Formula:** (Sum of marks)/(no. of subjects)\n",
        "**Sample Input:** {\"Krishna\":[67,68,69], \"Arjun\":[70,98,63], \"Malika\":[52,56,60]}\n",
        "**Sample Output:** Enter a name: Malika Average percentage mark: 56"
      ],
      "metadata": {
        "id": "Z4Lfz3x545Hb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "record = {\n",
        "    \"Krishna\": [67, 68, 69],\n",
        "    \"Arjun\": [70, 98, 63],\n",
        "    \"Malika\": [52, 56, 60]\n",
        "}\n",
        "name = input(\"Enter a name: \")\n",
        "if name in record:\n",
        "    marks = record[name]\n",
        "    average_percentage = sum(marks) / len(marks)\n",
        "    print(f\"Average percentage mark for {name}: {average_percentage:.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tlDWaqZCIGnd",
        "outputId": "574d5511-94b2-4045-80c7-e79503268a71"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a name: Krishna\n",
            "Average percentage mark for Krishna: 68.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "PROJECT- 4 => Given a string of n words, help Alex to find out how many times his name appears in the string.\n",
        "**Constraint:** 1 <= n <= 200\n",
        "**Sample Input:** Hi Alex Welcome Alex By Alex.\n",
        "**Sample Output:** 3"
      ],
      "metadata": {
        "id": "ov7AjU-5IZ_g"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sentence = input(\"Enter a string: \")\n",
        "name_to_find = \"Alex\"\n",
        "lower_sentence = sentence.lower()\n",
        "words = lower_sentence.split()\n",
        "count = words.count(name_to_find.lower())\n",
        "print(f\"{count}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QiKDu09IK21Q",
        "outputId": "1b997a4f-cb07-4ce8-c6c2-be7c1413d220"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a string: Hi Alex Welcome Alex By Alex\n",
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Functions/Modules/Packages**"
      ],
      "metadata": {
        "id": "CAUq38iiLUdq"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Hands on Assignment on Functions*"
      ],
      "metadata": {
        "id": "k00WNoyx2oRy"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. WAF to return the sum of all numbers in a list. Sample List: (8,2,3,0,7) Expected OutPut: 20"
      ],
      "metadata": {
        "id": "dGIf_KjH2z32"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def sum_list_elements(numbers):\n",
        "    \"\"\"Calculates the sum of all numbers in a list.\"\"\"\n",
        "    return sum(numbers)\n",
        "sample_list = [8,2,3,0,7]\n",
        "result = sum_list_elements(sample_list)\n",
        "print(f\"The sum of the numbers in the list {sample_list} is: {result}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EgVTMy294q8k",
        "outputId": "434e6774-a2c4-4724-8ba5-b8f8e0a8a49a"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The sum of the numbers in the list [8, 2, 3, 0, 7] is: 20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. WAF to return the reverse of a string.\n",
        "Sample String: \"1234abcd\"\n",
        "Expected Output: \"dcba4321\""
      ],
      "metadata": {
        "id": "Yah0-joO5SdS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def reverse_string(input_string):\n",
        "    \"\"\"Reverses a string.\"\"\"\n",
        "    return input_string[::-1]\n",
        "sample_string = \"1234abcd\"\n",
        "reversed_string = reverse_string(sample_string)\n",
        "print(f\"The reverse of the string '{sample_string}' is: '{reversed_string}'\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ePSHs6A55xaN",
        "outputId": "bfd9c69d-7074-4dca-ccb2-bb9d4ac10f89"
      },
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The reverse of the string '1234abcd' is: 'dcba4321'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. WAF to calculate and return the factorial of a number (a non-negative integer)."
      ],
      "metadata": {
        "id": "UyRqZZ9PFAFn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def calculate_factorial(num):\n",
        "  fact = 1\n",
        "  for i in range(1, num + 1):\n",
        "    fact = fact * i\n",
        "  return fact\n",
        "n = int(input(\"Enter a number: \"))\n",
        "res = calculate_factorial(n)\n",
        "print(f\"The factorial of {n} is: {res}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6snrj6DJFZYl",
        "outputId": "b78ed914-2f49-4841-add0-09cd92797dca"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 6\n",
            "The factorial of 6 is: 720\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. WAF that accepts a string and prints the no. of upper case letters and lower case letters in it."
      ],
      "metadata": {
        "id": "ur5qapv5HoW3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def count_upper_lower(string):\n",
        "    upper_count = 0\n",
        "    lower_count = 0\n",
        "    for char in string:\n",
        "        if char.isupper():\n",
        "            upper_count += 1\n",
        "        elif char.islower():\n",
        "            lower_count += 1\n",
        "    return upper_count, lower_count\n",
        "\n",
        "string = input(\"Enter the String: \")\n",
        "upper_count, lower_count = count_upper_lower(string)\n",
        "print(\"Uppercase count:\", upper_count)\n",
        "print(\"Lowercase count:\", lower_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YGj0OvuyIJnt",
        "outputId": "b54a8ef1-5ab7-4b66-96bd-6866a657f140"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the String: Hi, I am Here\n",
            "Uppercase count: 3\n",
            "Lowercase count: 6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. WAF to print the even no.s from a given list . List is passed to the function as an argument.\n",
        "Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]\n",
        "Expected Result: [2, 4, 6, 8]"
      ],
      "metadata": {
        "id": "v_4fppxUImyd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def even_num(input_list):\n",
        "  even_nums = []\n",
        "  for num in input_list:\n",
        "    if num % 2 == 0:\n",
        "      even_nums.append(num)\n",
        "  print(f\"Even numbers in the list: {even_nums}\")\n",
        "sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n",
        "even_num(sample_list)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t--M3sKMMkJI",
        "outputId": "e30b4208-33dc-4933-8124-c7e35c168788"
      },
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Even numbers in the list: [2, 4, 6, 8]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6. WAF that takes a number as a parameter and checks whether the no. is prime or not."
      ],
      "metadata": {
        "id": "FiQnDRMkNSqX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def check_prime(n):\n",
        "  if n < 2:\n",
        "    return False\n",
        "  for i in range(2,int(n**0.5)+1):\n",
        "    if n % i == 0:\n",
        "      return False\n",
        "  return True\n",
        "num = int(input(\"Enter a number: \"))\n",
        "res = check_prime(num)\n",
        "if res == True:\n",
        "  print(f\"{num} is a prime number\")\n",
        "else:\n",
        "  print(f\"{num} is not a prime number\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VmLUvTB8NnsN",
        "outputId": "a4220608-efb6-48e0-c94d-e902248fee7f"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 8\n",
            "8 is not a prime number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *MINI-PROJECTS*"
      ],
      "metadata": {
        "id": "_Yp6Wo3lSD82"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "PROJECT- 1 => WAF in python that accepts the hyphen-separated seq. of colors --------- alphabetically. **Constraint:** All the colors will be completely in either lower-case or upper-case. **Sample input 1:** green-red-yellow-black-white **Sample Output 1:** black-green-red-white-yellow  **Sample input 2:** PINK-BLUE-TAN-PURPLE **Sample Output 2:** BLUE-PINK-PURPLE-TAN"
      ],
      "metadata": {
        "id": "uHc87FoNKUCJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def sort_colors(colors):\n",
        "    color_list = colors.split('-')\n",
        "    color_list.sort()\n",
        "    return '-'.join(color_list)\n",
        "\n",
        "colors = input(\"Enter hyphen-separated colors: \")\n",
        "print(f\"Sorted colors: {sort_colors(colors)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2Z5vg3rpNMM2",
        "outputId": "cf269f0f-d02f-4b56-cd42-070c50ef76ef"
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter hyphen-separated colors: BLUE-PINK-PURPLE-TAN\n",
            "Sorted colors: BLUE-PINK-PURPLE-TAN\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "PROJECT- 2 => Create a python module with following functions: ispalindrome(name) , count_the_vowels(name) , frequency_of_letters(name) where name will be completely in either lower or upper case. Import module in another python script and test the functions by passing appr. inputs. **Sample Input 1:** bob **Sample Output 1:** Yes it is a palindrome. No. of vowels: 1 Frequency of letters: b-2, o-1  **Sample Input 2:** marcel bentok tanaka **Sample Output 1:** No it is not a palindrome. No. of vowels: 7 Frequency of letters: m-1, a-4, r-1, c-1, e-2, l-1, b-1, n-2, t-2, o-1, k-2"
      ],
      "metadata": {
        "id": "TaZIrTjTN3J8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile string_module.py\n",
        "\n",
        "def ispalindrome(name):\n",
        "    temp = name.replace(\" \", \"\")\n",
        "    return temp == temp[::-1]\n",
        "\n",
        "def count_the_vowels(name):\n",
        "    count = 0\n",
        "    vowels = \"aeiouAEIOU\"\n",
        "    for ch in name:\n",
        "        if ch in vowels:\n",
        "            count += 1\n",
        "    return count\n",
        "\n",
        "def frequency_of_letters(name):\n",
        "    freq = {}\n",
        "    for ch in name:\n",
        "        if ch != \" \":\n",
        "            freq[ch] = freq.get(ch, 0) + 1\n",
        "    return freq"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kwtu50GKUDJG",
        "outputId": "5975b1c1-ab8c-4dbd-f058-da67ff408dd0"
      },
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing string_module.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import string_module\n",
        "name = input(\"Enter a name/string: \")\n",
        "\n",
        "# Palindrome Check\n",
        "if string_module.ispalindrome(name):\n",
        "    print(\"Yes it is a palindrome.\")\n",
        "else:\n",
        "    print(\"No it is not a palindrome.\")\n",
        "\n",
        "# Vowel Count\n",
        "print(\"No. of vowels:\", string_module.count_the_vowels(name))\n",
        "\n",
        "# Frequency of Letters\n",
        "freq = string_module.frequency_of_letters(name)\n",
        "print(\"Frequency of letters:\")\n",
        "for key, value in freq.items():\n",
        "    print(f\"{key}-{value}\", end=\", \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "isTAvcahVWad",
        "outputId": "c6f4258b-3f1f-45ed-cdd9-b3f1cb66a789"
      },
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a name/string: marcel bentok tanaka\n",
            "No it is not a palindrome.\n",
            "No. of vowels: 7\n",
            "Frequency of letters:\n",
            "m-1, a-4, r-1, c-1, e-2, l-1, b-1, n-2, t-2, o-1, k-2, "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Command Line Arguments**"
      ],
      "metadata": {
        "id": "a0AGAVHNVxym"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Hands on Assignment on Command Line Arguments*"
      ],
      "metadata": {
        "id": "30yXWSA1UrRO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. WAP to accept two numbers as command line arguments and display their sum."
      ],
      "metadata": {
        "id": "vTWdNbqTU58c"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import sys\n",
        "a = input(\"Enter first number: \")\n",
        "b = input(\"Enter second number: \")\n",
        "sys.argv = ['sum.py',a,b]\n",
        "num1 = int(sys.argv[1])\n",
        "num2 = int(sys.argv[2])\n",
        "sum = num1 + num2\n",
        "print(f\"The sum of {num1} and {num2} is: {sum}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QISi2oneVJkL",
        "outputId": "d508b26c-5f49-4062-f5b9-cbea6450f62a"
      },
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: 10\n",
            "Enter second number: 20\n",
            "The sum of 10 and 20 is: 30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. WAP to accept a welcome message through command line Arguments and display the file name along with the welcome message."
      ],
      "metadata": {
        "id": "KENL-qFratCT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import sys\n",
        "msg = input(\"Enter a welcome message: \")\n",
        "sys.argv = ['welcome.py',msg]\n",
        "print(f\"Welcome Message: {sys.argv[1]} {sys.argv[0]}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pJ14wkVIRXmw",
        "outputId": "48f32e62-6a13-4e97-983e-089148310ac0"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a welcome message: Welcome to my house\n",
            "Welcome Message: Welcome to my house welcome.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. WAP  to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them."
      ],
      "metadata": {
        "id": "j_PBycpjTYf2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import sys\n",
        "sys.argv = ['prime_sum.py', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']\n",
        "def is_prime(n):\n",
        "    if n < 2:\n",
        "        return False\n",
        "    for i in range(2, int(n**0.5) + 1):\n",
        "        if n % i == 0:\n",
        "            return False\n",
        "    return True\n",
        "nums_str = sys.argv[1:11]\n",
        "print(f\"Numbers received: {nums_str}\")\n",
        "sum_primes = 0\n",
        "for i in range(1, 11):\n",
        "  num = int(sys.argv[i])\n",
        "  if is_prime(num):\n",
        "    sum_primes += num\n",
        "prime_num = [num for num in range(1, 11) if is_prime(num)]\n",
        "print(\"Among Them Prime numbers are =\", prime_num)\n",
        "print(\"Sum of prime numbers =\", sum_primes)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ckDfMAmCU8BH",
        "outputId": "3c189e87-0db7-4165-8cce-d506c770a2a8"
      },
      "execution_count": 64,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Numbers received: ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11']\n",
            "Among Them Prime numbers are = [2, 3, 5, 7]\n",
            "Sum of prime numbers = 28\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *MINI-PROJECTS*"
      ],
      "metadata": {
        "id": "MR1gC8rPXQTx"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "PROJECT => Through Command line arguments ---------- . Output your final happiness at the end.  **Sample Input 1:** 3-1 5-7 1-5-3-8\n",
        "**Sample Output 1:** 1  **Sample Input 2:** 60-77-34-5-2 44-11-99-3 77-15-13-2-34-3 **Sample Output 2:** 2"
      ],
      "metadata": {
        "id": "AoxTjdGAX6Bp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import sys\n",
        "a = input(\"Enter first range: \")\n",
        "b = input(\"Enter second range: \")\n",
        "c = input(\"Enter third range: \")\n",
        "\n",
        "sys.argv = [ \"happiness.py\", a, b, c]\n",
        "A = set(map(int, sys.argv[1].split('-')))\n",
        "B = set(map(int, sys.argv[2].split('-')))\n",
        "arr = list(map(int, sys.argv[3].split('-')))\n",
        "happiness = 0\n",
        "\n",
        "for num in arr:\n",
        "    if num in A:\n",
        "        happiness += 1\n",
        "    elif num in B:\n",
        "        happiness -= 1\n",
        "print(happiness)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IueDI-cIafsT",
        "outputId": "bb3c291f-fa9b-45c1-ac48-f2c8172f9f42"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first range: 60-77-34-5-2\n",
            "Enter second range: 44-11-99-3\n",
            "Enter third range: 77-15-13-2-34-3\n",
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **IO Operations**"
      ],
      "metadata": {
        "id": "WkSONZUfcAMR"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Hands on Assignment on IO Operations*"
      ],
      "metadata": {
        "id": "yYxPIm2wcbZB"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. WAP to read the entire content from a txt file and display it to the user."
      ],
      "metadata": {
        "id": "1-gPEUmPcptr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"sample.txt\", \"w\") as file:\n",
        "    file.write(\"Hello World\\nWelcome to Python\\nFile Handling Example\\nI am Raghav\\nThis is wipro Data Science Class\")"
      ],
      "metadata": {
        "id": "78EjvThh93AI"
      },
      "execution_count": 66,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"sample.txt\", \"r\") as file:\n",
        "    print(file.read())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vu4UV-iZ98MZ",
        "outputId": "a67b9e6e-63a2-4d28-9c55-518ee8922090"
      },
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World\n",
            "Welcome to Python\n",
            "File Handling Example\n",
            "I am Raghav\n",
            "This is wipro Data Science Class\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. WAP to first read n lines from a txt file. Get n as user input."
      ],
      "metadata": {
        "id": "kHveZ79U-T6d"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"sample.txt\", \"r\") as file:\n",
        "    n = int(input(\"Enter the number of lines to read: \"))\n",
        "    for i in range(n):\n",
        "        print(\"\\n\",file.readline())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X8zOtwcC-k0y",
        "outputId": "23df5342-696a-45ec-b632-c835522bf7f4"
      },
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the number of lines to read: 3\n",
            "\n",
            " Hello World\n",
            "\n",
            "\n",
            " Welcome to Python\n",
            "\n",
            "\n",
            " File Handling Example\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. WAP to accept input from user and append it to a txt file."
      ],
      "metadata": {
        "id": "4D5PM98p_J1M"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"sample.txt\", \"a\") as file:\n",
        "    user_input = input(\"Enter some text: \")\n",
        "    file.write(user_input)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TiPOfx8fAMhD",
        "outputId": "57d17e5e-55de-4ff8-83f4-e0dbc645adee"
      },
      "execution_count": 69,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter some text: Hi, I am On\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"sample.txt\", \"r\") as file:\n",
        "    print(file.read())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xf52OGveAxgf",
        "outputId": "f34ae37a-8dc2-445c-d328-2ebef13a7adf"
      },
      "execution_count": 70,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World\n",
            "Welcome to Python\n",
            "File Handling Example\n",
            "I am Raghav\n",
            "This is wipro Data Science ClassHi, I am On\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. WAP to read contents from a txt file line by line and store each line into a list."
      ],
      "metadata": {
        "id": "rsijjmdCA3v7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"sample.txt\", \"r\") as file:\n",
        "    lines = file.readlines()\n",
        "    print(lines)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PQ9u_PPpDeFM",
        "outputId": "e17c44c0-4715-4361-97f4-22ff77fc28c6"
      },
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hello World\\n', 'Welcome to Python\\n', 'File Handling Example\\n', 'I am Raghav\\n', 'This is wipro Data Science ClassHi, I am On']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. WAP to find the longest word from the txt file contents, assuming that the file will have only one longest word in it."
      ],
      "metadata": {
        "id": "Yh4kQZUaDptE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"sample.txt\", \"r\") as file:\n",
        "    words = file.read().split()\n",
        "    longest_word = max(words, key=len)\n",
        "    print(\"Longest word:\", longest_word)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ILSJU77tJxhh",
        "outputId": "8bf539a3-b4e2-45c8-ddb9-48039731f636"
      },
      "execution_count": 72,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Longest word: Handling\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6. WAP to count the frequency of a user entered word in a txt file."
      ],
      "metadata": {
        "id": "HJPf41qXJ60V"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"sample.txt\", \"r\") as file:\n",
        "    content = file.read()\n",
        "    word_to_count = input(\"Enter the word to count: \")\n",
        "    count = content.count(word_to_count)\n",
        "    print(\"Frequency of word: \",count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-KxtBjncKJjj",
        "outputId": "bfb9a53b-29f4-421c-a6aa-96cf585e8972"
      },
      "execution_count": 73,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the word to count: Hi\n",
            "Frequency of word:  1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *MINI-PROJECTS*"
      ],
      "metadata": {
        "id": "C-jdP61LKguw"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "PROJECT => Your friend has sent --------------- Python code. Hints to find the secret message :\n",
        "1. The no. of lines in the file tells you the meeting time. **Note:** 1 <= no. of lines <= 24 If no. of lines > 12 , you need to convert it to 12 hour format. For Ex:,  \n",
        "*   if no. of lines = 15 , then meeting time is 3 PM\n",
        "*   if no. of lines = 10 , then meeting time is 10 AM\n",
        "\n",
        "2. The word appearing for the max. no. of times tells you the meeting place. **Note:** Meeting place will be a street name. For Ex:,\n",
        "\n",
        "*   If the word Oxford, appears for the maximum no. of times, then meeting time is Oxford Street\n",
        "*   If the word Park, appears for the maximum no. of times, then meeting time is Park Street\n",
        "\n",
        "**Sample Input 1:** Sample.txt = Cricket, a bat-and-ball park game ------------- park roles.\n",
        "\n",
        "**Sample Output 1:**\n",
        "*   Meeting time: 9 AM\n",
        "*   Meeting place: Park Street\n",
        "\n",
        "**Sample Input 2:** Sample.txt = Royal Enfield ------- models.\n",
        "\n",
        "**Sample Output 2:**\n",
        "*   Meeting time: 8 PM\n",
        "*   Meeting place: Apollo Street\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "0veo_n2OQG9B"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"Sample.txt\", \"w\") as file:\n",
        "    file.write(\"Cricket, a bat-and-ball park game played between two teams of eleven park\\nplayers on a field at the park center of which is a 20-metre(22-yard) pitch with\\na wicket at each end, each park comprising two bails balanced on three stumps.\\nThe batting park scores runs by striking the ball bowled at the park wicket with\\nthe park bat, while the bowling and park fielding side tries to prevent this and\\ndismiss each park player (so they are 'out').Means of park include being\\nbowled, when the ball hits the park and dislodges the bails, and by the fielding\\nside park the ball after it is hit by the bat, but before it hits the park. When ten\\npark have been dismissed, the innings ends and the teams park roles. \")"
      ],
      "metadata": {
        "id": "NXb2K4t9zVUI"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "filename = input(\"Enter the file name: \")\n",
        "with open(filename, \"r\") as file:\n",
        "  lines = file.readlines()\n",
        "\n",
        "# Meeting Time\n",
        "line_count = len(lines)\n",
        "if line_count <= 12:\n",
        "  meeting_time = str(line_count) + \" AM\"\n",
        "else:\n",
        "  meeting_time = str(line_count - 12) + \" PM\"\n",
        "\n",
        "# Meeting Place\n",
        "freq = {}\n",
        "for line in lines:\n",
        "  words = line.split()\n",
        "  for word in words:\n",
        "    word = word.strip(\".,!?;:\").lower()\n",
        "    if word in freq:\n",
        "      freq[word] += 1\n",
        "    else:\n",
        "      freq[word] = 1\n",
        "max_word = max(freq, key=freq.get)\n",
        "print(\"Meeting time: \", meeting_time)\n",
        "print(\"Meeting place: \", max_word.capitalize(), \"Street\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DbclgcIW3I3S",
        "outputId": "dd4b360e-cf1c-4c03-f5d3-4cb17008fe24"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the file name: Sample.txt\n",
            "Meeting time:  9 AM\n",
            "Meeting place:  Park Street\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Exception Handling**"
      ],
      "metadata": {
        "id": "vPL37S-rgiVG"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Hands on Assignment on Exception Handling*"
      ],
      "metadata": {
        "id": "CnCXJFjLhiyG"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. WAP to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result."
      ],
      "metadata": {
        "id": "PRXATf4FhvJ8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = int(input(\"Enter first number: \"))\n",
        "b = int(input(\"Enter second number: \"))\n",
        "try:\n",
        "    result = a / b\n",
        "    print(\"Result:\", result)\n",
        "except ZeroDivisionError:\n",
        "    print(\"Error: Division by zero is not allowed.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eLY48jXTiP3l",
        "outputId": "8d797a6c-4f44-4b32-952b-ad738bc7d108"
      },
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: 8\n",
            "Enter second number: 7\n",
            "Result: 1.1428571428571428\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. WAP to accept a number from user and check whether it's prime or not. If user enters anything other than number, handle the exception and print the error message."
      ],
      "metadata": {
        "id": "KPFk7vnBl5sx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num = input(\"Enter a number: \")\n",
        "try:\n",
        "    num = int(num)\n",
        "    if num < 2:\n",
        "        print(f\"{num} is not a prime number.\")\n",
        "    else:\n",
        "        for i in range(2, int(num**0.5 + 1)):\n",
        "          if num % i == 0:\n",
        "            print(f\"{num} is not a prime number.\")\n",
        "            break\n",
        "        else:\n",
        "            print(f\"{num} is a prime number.\")\n",
        "except ValueError:\n",
        "    print(\"Error: Invalid input. Please enter a valid number.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "srUXviUn8Ns_",
        "outputId": "32143630-f05f-487e-e0d6-52bba28f077c"
      },
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 3\n",
            "3 is a prime number.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. WAP to accept the file name to be opened from the user, if file exist print the contents of the file in title case or handle the exception and print an error message."
      ],
      "metadata": {
        "id": "4Wa-zdZM8o7i"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "file = input(\"Enter the file name: \")\n",
        "try:\n",
        "    with open(file, 'r') as f:\n",
        "        contents = f.read()\n",
        "        print(contents.title())\n",
        "except FileNotFoundError:\n",
        "    print(f\"Error: The file '{file}' does not exist.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tjif1V5D9Nwp",
        "outputId": "9711ebd5-674d-4761-c0b8-2b5cbb50f9b1"
      },
      "execution_count": 77,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the file name: sample.txt\n",
            "Hello World\n",
            "Welcome To Python\n",
            "File Handling Example\n",
            "I Am Raghav\n",
            "This Is Wipro Data Science Classhi, I Am On\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message."
      ],
      "metadata": {
        "id": "Y0viBDd-_Lmn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Li = [10, -5, 20, -15, 30, -25, 40, -35, 50, -45]\n",
        "try:\n",
        "    index = int(input(\"Enter an index (0-9): \"))\n",
        "    if 0 <= index < len(Li):\n",
        "        num = Li[index]\n",
        "        if num > 0:\n",
        "            print(f\"The number at index {index} is {num}, which is positive.\")\n",
        "        elif num < 0:\n",
        "            print(f\"The number at index {index} is {num}, which is negative.\")\n",
        "        else:\n",
        "            print(f\"The number at index {index} is {num}, which is zero.\")\n",
        "    else:\n",
        "        print(f\"Error: Index {index} is out of bounds. Please enter an index between 0 and {len(Li) - 1}.\")\n",
        "except ValueError:\n",
        "    print(\"Error: Invalid input. Please enter an integer for the index.\")\n",
        "except Exception as e:\n",
        "    print(f\"An unexpected error occurred: {e}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "loV_1Xz8AZYc",
        "outputId": "e71ab084-a579-46f7-eaf2-b6b5a295cf82"
      },
      "execution_count": 79,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter an index (0-9): 11\n",
            "Error: Index 11 is out of bounds. Please enter an index between 0 and 9.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *MINI-PROJECTS*"
      ],
      "metadata": {
        "id": "lTacH5O2BEL2"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "PROJECT => You saved --------- market. You need to know\n",
        "\n",
        "1.   How many items did you purchase ?\n",
        "2.   How many items are free ?\n",
        "3.   What is the Total amount you had to pay ?\n",
        "4.   What is the discount amount ?\n",
        "5.   What is the final amount did you pay after the discount ?\n",
        "Help ------------- runtime.\n",
        "**Sample Input 1:** Purchase-1.txt =\n",
        "\n",
        "*   Chocolate 50\n",
        "*   Biscuit 35\n",
        "\n",
        "\n",
        "*   Icecream 50\n",
        "(blank line) Discount 5\n",
        "**Sample Output 1:**\n",
        "*   Enter the file name: Purchase-1\n",
        "*   No of items purchased: 3\n",
        "*   No of free items: 0\n",
        "*   Amount to pay: 135\n",
        "*   Discount given: 5\n",
        "*   Final amount paid: 130\n",
        "\n",
        "**Sample Input 2:** Purchase-1.txt =\n",
        "\n",
        "*   Chocolate 50\n",
        "*   Biscuit 35\n",
        "*   Icecream 50\n",
        "*   Rice 100\n",
        "*   Chicken 250\n",
        "(blank line)\n",
        "*   Perfume free\n",
        "*   Soup free\n",
        "(blank line)\n",
        "Discount 80\n",
        "**Sample Output 2:**\n",
        "*   Enter the file name: Purchase-1\n",
        "*   No of items purchased: 5\n",
        "*   No of free items: 2\n",
        "*   Amount to pay: 485\n",
        "*   Discount given: 80\n",
        "*   Final amount paid: 405\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "7QaWOJWPkPDc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"Purchase-1.txt\", \"w\") as file:\n",
        "    file.write(\"Chocolate 50\\nBiscuit 35\\nIcecream 50\\nRice 100\\nChicken 250\\n\\nPerfume free\\nSoup free\\n\\nDiscount 80\")"
      ],
      "metadata": {
        "id": "VWG-L2HdpD8g"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "    filename = input(\"Enter the file name: \") + \".txt\"\n",
        "    purchased = 0\n",
        "    free_items = 0\n",
        "    amount = 0\n",
        "    discount = 0\n",
        "    with open(filename, \"r\") as file:\n",
        "        for line in file:\n",
        "            line = line.strip()\n",
        "            if line == \"\":\n",
        "                continue\n",
        "            if line.startswith(\"Discount\"):\n",
        "                discount = int(line.split()[1])\n",
        "            else:\n",
        "                parts = line.split()\n",
        "\n",
        "                if parts[-1].lower() == \"free\":\n",
        "                    free_items += 1\n",
        "                else:\n",
        "                    purchased += 1\n",
        "                    amount += int(parts[-1])\n",
        "    print(\"No of items purchased:\", purchased)\n",
        "    print(\"No of free items:\", free_items)\n",
        "    print(\"Amount to pay:\", amount)\n",
        "    print(\"Discount given:\", discount)\n",
        "    print(\"Final amount paid:\", amount - discount)\n",
        "\n",
        "except FileNotFoundError:\n",
        "    print(\"File does not exist.\")\n",
        "except ValueError:\n",
        "    print(\"Invalid data in file.\")\n",
        "except Exception as e:\n",
        "    print(\"An error occurred:\", e)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E0pu8ktlp8xQ",
        "outputId": "3cc58d76-3b4e-4d20-e993-77d26c5f72e6"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the file name: Purchase-1\n",
            "No of items purchased: 5\n",
            "No of free items: 2\n",
            "Amount to pay: 485\n",
            "Discount given: 80\n",
            "Final amount paid: 405\n"
          ]
        }
      ]
    }
  ]
}