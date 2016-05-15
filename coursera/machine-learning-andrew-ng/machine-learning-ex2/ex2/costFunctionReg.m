function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
theta_reg_len = length(theta);

predictions = sigmoid(X*theta);
Error = predictions - y;

predictions_init = sigmoid(X(:,1)*theta(1));
Error_init = predictions_init - y;
J = 1/m * sum((-y.*log(predictions_init) - ((1-y).*log(1-predictions_init))));

predictions_rest = sigmoid(X(:,2:theta_reg_len)*theta(2:theta_reg_len));
Error_rest = predictions_rest - y;
% J = J + 1/m * sum((-y.*log(predictions_rest) - ((1-y).*log(1-predictions_rest)))) + lambda/(2*m)*sum(theta(2:theta_reg_len).^2);

J = 1/m * sum((-y.*log(predictions) - ((1-y).*log(1-predictions)))) + lambda/(2*m)*sum(theta(2:theta_reg_len).^2);

grad(1) = transpose((1/m) * sum(Error_init.*X(:,1)));

reg_param = lambda/m*theta(2:theta_reg_len);
% fprintf('Reg param: %f %f\n', size(reg_param));
logistic_grad = transpose((1/m) * sum(Error_rest.*X(:,2:theta_reg_len)));
% logistic_grad = transpose((1/m) * sum(Error.*X));
% fprintf('logistic_grad: %f %f\n', size(logistic_grad));
grad(2:theta_reg_len) = logistic_grad + reg_param;

% grad = transpose(grad);
% fprintf('grad param: %f %f\n', grad);
% =============================================================

end
