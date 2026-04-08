import dotenv from 'dotenv';

dotenv.config();

export const APP_VERSION = process.env.APP_VERSION || '0.0.0';
export const ALLOWED_ORIGIN = process.env.ALLOWED_ORIGIN || '*';
export const PORT = parseInt(process.env.PORT || '3000', 10);