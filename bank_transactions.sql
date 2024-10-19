CREATE TABLE bank_transactions (
    transaction_id INT PRIMARY KEY,
    date DATE,
    amount DECIMAL(10, 2),
    description VARCHAR(255)
);

INSERT INTO transactions (transaction_id, date, amount, description) VALUES
(1, '2024-10-01', 500.00, 'Salary Deposit'),
(2, '2024-10-02', -150.00, 'Grocery Purchase'),
(3, '2024-10-03', -200.00, 'Restaurant'),
(4, '2024-10-04', -50.00, 'Taxi'),
(5, '2024-10-05', -20.00, 'Coffee Shop'),
(6, '2024-10-06', 1000.00, 'Freelance Payment'),
(7, '2024-10-07', -75.00, 'Gym Membership'),
(8, '2024-10-08', -200.00, 'Electricity Bill'),
(9, '2024-10-09', -500.00, 'Rent Payment'),
(10, '2024-10-10', -120.00, 'Online Shopping'),
(11, '2024-10-19', 105.00, NULL),
(12, '2024-10-18', 155.50, NULL),
(13, '2024-10-17', NULL, NULL),
(14, '2024-10-16', 198.00, NULL),
(15, '2024-10-15', 180.25, NULL),
(16, '2024-10-14', 295.75, NULL),
(17, '2024-10-13', NULL, NULL),
(18, '2024-10-12', 245.50, NULL),
(19, '2024-10-11', 185.00, NULL),
(20, '2024-10-10', 410.25, NULL),
(21, '2024-10-09', NULL, NULL),
(22, '2024-10-08', 225.75, NULL),
(23, '2024-10-07', 280.50, NULL),
(24, '2024-10-06', 160.00, NULL),
(25, '2024-10-05', NULL, NULL),
(26, '2024-10-04', 355.25, NULL),
(27, '2024-10-03', 245.00, NULL),
(28, '2024-10-02', 185.50, NULL),
(29, '2024-10-01', NULL, NULL),
(30, '2024-09-30', 280.75, NULL),
(31, '2024-09-29', 215.25, NULL),
(32, '2024-09-28', 195.00, NULL),
(33, '2024-09-27', NULL, NULL),
(34, '2024-09-26', 325.50, NULL),
(35, '2024-09-25', 265.75, NULL),
(36, '2024-09-24', 235.25, NULL),
(37, '2024-09-23', NULL, NULL),
(38, '2024-09-22', 285.00, NULL),
(39, '2024-09-21', 200.50, NULL),
(40, '2024-09-20', 155.75, NULL),
(41, '2024-09-19', NULL, NULL),
(42, '2024-09-18', 315.25, NULL),
(43, '2024-09-17', 230.00, NULL),
(44, '2024-09-16', 180.50, NULL),
(45, '2024-09-15', NULL, NULL),
(46, '2024-09-14', 345.75, NULL),
(47, '2024-09-13', 265.50, NULL),
(48, '2024-09-12', 205.25, NULL),
(49, '2024-09-11', NULL, NULL),
(50, '2024-09-10', 290.00, NULL);
