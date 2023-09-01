export interface LoginRequest {
    username: string;
    password: string;
  }
  
export interface LoginResponse {
    access_token: string;
    token_type: string;
    // Additional properties for successful login response
  }
  
export interface LoginError {
    error: string;
    // Additional properties for error response
  }
