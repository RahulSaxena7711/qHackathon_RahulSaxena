#Let us first try to make a function that initializes the quantum state
import numpy as np
import math as mt
import random


def inititate(dim, list):#initiates the quantum state vector and normalizes it
    qstate = []
    sqsum = 0
    for i in range(dim):
        qstate.append(list[i])
        sqsum = sqsum + (list[i])*(np.conj(list[i]))
    rs = mt.sqrt(sqsum)
    for i in range(dim):
        qstate[i] = qstate[i] / rs
    return qstate


def pauli_x(qubitnum, qstate):#PauliX operation
    operand = np.array(qstate[(2*qubitnum):(2*qubitnum+2)])
    operator = np.array([[0, 1], [1, 0]])
    res = operator*operand
    qstate[(2*qubitnum):(2*qubitnum+1)] = [res[0], res[1]]
    return qstate


def pauli_y(qubitnum, qstate):#PauliY operation
    operand = np.array(qstate[(2*qubitnum):(2*qubitnum+2)])
    operator = np.array([[0, -1j], [1j, 0]])
    res = operator*operand
    qstate[(2*qubitnum):(2*qubitnum+1)] = [res[0], res[1]]
    return qstate


def pauli_z(qubitnum, qstate):#PauliZ operation
    operand = np.array(qstate[(2*qubitnum):(2*qubitnum+2)])
    operator = np.array([[1, 0], [0, -1]])
    res = operator*operand
    qstate[(2*qubitnum):(2*qubitnum+1)] = [res[0], res[1]]
    return qstate


def hadamard(qubitnum, qstate):#Hadamard operation
    operand = np.array(qstate[(2*qubitnum):(2*qubitnum+2)])
    operator = np.array([[1/mt.sqrt(2), 1/mt.sqrt(2)], [1/mt.sqrt(2), -1/mt.sqrt(2)]])
    res = operator*operand
    qstate[(2*qubitnum):(2*qubitnum+1)] = [res[0], res[1]]
    return qstate


def cnot(qubitnum1, qubitnum2, qstate):#CNOT operation. First qubit is the controlling bit.
    operand = np.array([qstate[(2*qubitnum1)], qstate[(2*qubitnum1+1)], qstate[2*qubitnum2], qstate[2*qubitnum2+1]])
    operator = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    res = operator*operand
    qstate[(2 * qubitnum1):(2 * qubitnum1 + 1)] = [res[0], res[1]]
    qstate[(2 * qubitnum2):(2 * qubitnum2 + 1)] = [res[2], res[3]]
    return qstate


if __name__ == "__main__":
    qubNum = int(input("Enter the number of qubits in the system"))
    dim = 2*qubNum
    quantState = []
    print("Enter probability amplitudes, the state will be automatically normalized")
    for i in range(dim):
        val = complex(input())
        quantState.append(val)
    print("Enter which operation due you want to apply.\n")
    print("x: PauliX\ny: PauliY\nz: PauliZ\nh: Hadamard\nc: CNOT\n")
    gate = input()
    if gate == 'x':
        qubit = int(input("On which qubit do you want to apply the gate? (number starts from 0)"))
        quantState = pauli_x(qubit, quantState)
    elif gate == 'y':
        qubit = int(input("On which qubit do you want to apply the gate? (number starts from 0)"))
        quantState = pauli_y(qubit, quantState)
    elif gate == 'z':
        qubit = int(input("On which qubit do you want to apply the gate? (number starts from 0)"))
        quantState = pauli_z(qubit, quantState)
    elif gate == 'h':
        qubit = int(input("On which qubit do you want to apply the gate? (number starts from 0)"))
        quantState = hadamard(qubit, quantState)
    elif gate == 'c':
        qubit1 = int(input("Which qubit should be the controlling bit? (number starts from 0)"))
        qubit2 = int(input("On which qubit do you want to apply the gate? (number starts from 0)"))
        quantState = cnot(qubit1, qubit2, quantState)
    else:
        print("Wrong input. Program will terminate.")
        exit(0)
    decision = input("Want to see the final quantum state: q\nWant to measure a qubit: m\n")
    if decision == 'q':
        print("This is the final state:\n")
        print(quantState)
    elif decision == 'm':
        probAmps = []
        sequence = []
        for j in range(dim):
            probAmps.append(quantState[j]*(np.conj(quantState[j])))
        for j in range(dim):
            vect = []
            for k in range(dim):
                if j == k:
                    vect.append(1)
                else:
                    vect.append(0)
            sequence.append(vect)
        measured = random.choices(sequence, probAmps)
        print(measured)


